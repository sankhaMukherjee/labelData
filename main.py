import os

from bokeh.layouts import column, row
from bokeh.plotting import curdoc
from bokeh.models import Button, Select

from utils import innerPlot as iP

folder    = 'labelData/data'
fileNames = [f for f in os.listdir(folder) if f.endswith('.txt')]
fileName  = fileNames[0]

#-------------------------------------------------------
# Generate patient selection schema
#-------------------------------------------------------
def updatePatientCallback(attr, oldFile, newFile):
    entirePage.children[1] = iP.createInnerPlot(folder, newFile)
    return

dataSelect = Select(
    title   = 'Select Data',
    options = fileNames)

dataSelect.on_change( 'value', updatePatientCallback )

#-------------------------------------------------------
# Generate information about the first patient
#-------------------------------------------------------
innerPlot = iP.createInnerPlot(folder, fileName)

entirePage = column([
    dataSelect, innerPlot
])

curdoc().add_root(entirePage)

curdoc().title = "labelData"
