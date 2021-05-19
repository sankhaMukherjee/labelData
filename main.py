import os

from bokeh.layouts import column, row
from bokeh.plotting import curdoc
from bokeh.models import Button, Select

from utils import innerPlot as iP

folder    = 'labelData/data'
fileNames = [f for f in os.listdir(folder) if f.endswith('.txt')]
fileName  = fileNames[0]

createInnerPlot = iP.CreaterInnerPlot()

#-------------------------------------------------------
# Generate patient selection schema
#-------------------------------------------------------
def updatePatientCallback(attr, oldFile, newFile):
    entirePage.children[1] = createInnerPlot(folder, newFile)
    fileName = newFile
    return

dataSelect = Select(
    title   = 'Select Data',
    options = fileNames)

dataSelect.on_change( 'value', updatePatientCallback )

def increaseCallback():
    
    selects = iP.getSelects( entirePage.children[1].children[1].children )
    print(selects)

    createInnerPlot.toAddText(selects)
    entirePage.children[1] = createInnerPlot(folder, fileName)
    
    return

addButton = Button(label='Add Sentence Outer')
addButton.on_click( increaseCallback )

#-------------------------------------------------------
# Generate information about the first patient
#-------------------------------------------------------
innerPlot = createInnerPlot(folder, fileName)

entirePage = column([
    dataSelect, innerPlot, addButton
])

curdoc().add_root(entirePage)

curdoc().title = "labelData"
