import logging
from utils import dataIO as dIO

import numpy as np
import os

from bokeh.plotting import figure
from bokeh.layouts import column, row

from bokeh.models import Div
from bokeh.models import Toggle, Select, Button, MultiChoice

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, TableColumn, CheckboxEditor


# This is a basic logger. You might want to configure
# it to a more complex logger depending upon what you
# want.
logger = logging.getLogger()

config = {
    'select-width'   : 20,
    'textData-width' : 1000,
    'label-width'    : 300,
    'total-width'    : 1400
}

def getSelects( rowVals ):

    actives = [ r.children[0].active for r in rowVals ]

    return actives

class CreaterInnerPlot:

    def __init__(self):

        self.labels = [
            'mood - agitated',
            'mood - happy',
            'mood - sad',
            'affect - constricted',
            'affect - labile',
            'suicidal - ideation present',
            'suicidal - ideation with intent'
        ]

        self.currentFile = None
        self.rowVals = []
        self.userFeedback  = Div(text='initialized properly')
        self.listOfStrings = [f'some string i = {i}' for i in range(10)]
        self.generateRows(self.listOfStrings)

        self.finalResult = column([ column(self.rowVals), self.userFeedback])

        return 

    def toAddText(self, forUpdates):

        newStrings = []
        for u, s in zip(forUpdates, self.listOfStrings):
            newStrings.append(s)
            if u:
                newStrings.append(s)
        
        self.listOfStrings = newStrings
        self.generateRows( self.listOfStrings )
        self.finalResult = column([ column(self.rowVals), self.userFeedback])

        return
    
    def getLabel(self, string):

        if 'happy' in string:
            return self.labels[1]
        else:
            return np.random.choice( self.labels )

    def createRowVal(self, text):

        select      = Toggle( label='', width=config['select-width'], height=20 )
        textData    = Div( text=text,   width=config['textData-width'], height=20  )
        value       = MultiChoice(value=[self.getLabel(text)], options=self.labels, width=config['label-width'])
        # value       = Select( title = '', value = self.getLabel(text), options=self.labels, width=config['label-width']  )
    
        result = row([select, value, textData], width=config['total-width'])

        self.rowVals.append( result )

        return result

    def generateRows(self, listOfStrings):

        self.rowVals = []
        for s in listOfStrings:
            self.createRowVal(s)

        return

    def createFinalResult(self, listOfStrings):

        self.listOfStrings = listOfStrings
        self.generateRows( self.listOfStrings )
        self.finalResult = column([ column(self.rowVals), self.userFeedback])

        return

    def __call__(self, folder, newFile):

        try:
            
            if self.currentFile != os.path.join(folder, newFile):
                self.currentFile = os.path.join(folder, newFile)
                listOfStrings = []
                with open(self.currentFile) as f:
                    listOfStrings = [f'{i:4d}|{l}' for i, l in enumerate(f)]
                    self.createFinalResult(listOfStrings)
            else:
                self.createFinalResult(self.listOfStrings)

            return self.finalResult

        except Exception as e:
            logger.error(f'Unable to generate a plot: {e}')
            return column([Div(text=f'Problem with generating the plot: {e}')])

        return