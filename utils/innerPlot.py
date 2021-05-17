import logging
from utils import dataIO as dIO

from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.models import Div


# This is a basic logger. You might want to configure
# it to a more complex logger depending upon what you
# want.
logger = logging.getLogger()

def createInnerPlot(folder, fileName):

    try:
        TOOLS = "pan,box_zoom,reset"
        fig = figure(tools=TOOLS, width=900, height=200, toolbar_location="above")
        x = dIO.getData(folder, fileName)
        fig.circle(x, x, fill_color='red', line_color='red', size=6)

        userFeedback = Div(text='initialized properly')

        toReturn = column([ fig, userFeedback ])

        return toReturn

    except Exception as e:
        logger.error(f'Unable to generate a plot: {e}')
        toReturn = column([
            Div(text=f'Problem with generating the plot: {e}')])

        return toReturn


    return 
    