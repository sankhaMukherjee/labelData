import logging
from utils import dataIO as dIO

import numpy as np

from bokeh.plotting import figure
from bokeh.layouts import column, row

from bokeh.models import Div
from bokeh.models import Toggle, Select, Button

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, TableColumn, CheckboxEditor


# This is a basic logger. You might want to configure
# it to a more complex logger depending upon what you
# want.
logger = logging.getLogger()

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

        self.rowVals = []
        self.userFeedback  = Div(text='initialized properly')
        self.addButton = Button(label='add Sentence')
        self.listOfStrings = [f'string value = {i}' for i in range(10)]
        self.generateRows(self.listOfStrings)

        self.addButton.on_click( self.toAddText )
        self.finalResult = column([ self.addButton, column(self.rowVals), self.userFeedback])

        return 

    def toAddText(self, forUpdates=None):

        if forUpdates is None:
            forUpdates = [self.rowVals[i].children[0].active for i, s in enumerate(self.listOfStrings)]

        print(forUpdates)
        newStrings = []
        for u, s in zip(forUpdates, self.listOfStrings):
            newStrings.append(s)
            if u:
                newStrings.append(s)
        
        self.listOfStrings = newStrings
        self.generateRows( self.listOfStrings )
        self.finalResult = column([ self.addButton, column(self.rowVals), self.userFeedback])

        return
    
    def getLabel(self, string):

        if 'happy' in string:
            return self.labels[1]
        else:
            return np.random.choice( self.labels )

    def createRowVal(self, text):

        select      = Toggle( label='select', width=60, height=20 )
        textData    = Div( text=text, width=100, height=20  )
        value       = Select( title = '', value = self.getLabel(text), options=self.labels  )
    
        result = row([select, textData, value], width=600)

        self.rowVals.append( result )

        return result

    def generateRows(self, listOfStrings):

        self.rowVals = []
        for s in listOfStrings:
            self.createRowVal(s)

        return

    def __call__(self, folder, newFile):

        try:
            return self.finalResult

        except Exception as e:
            logger.error(f'Unable to generate a plot: {e}')
            return column([Div(text=f'Problem with generating the plot: {e}')])

        return