import logging, os

logger = logging.getLogger()

def getData(folder, fileName):
    '''read data from file

    This function is used primarily for getting specific
    data from the file/folder location available. Ideally
    this is going to be changed in a real application to
    reflect real sources of data (wherever they are located)

    Parameters
    ----------
    folder : str
        folder where the data file is located
    fileName : str
        The name of the file that contains the data

    Returns
    -------
    list of integers
        This returns a list of integers that represents the
        data that is ultimately going to be plotted or displayed.
    '''

    try:
        with open( os.path.join(folder, fileName) ) as f:
            data = [int(l.strip()) for l in f]

        return data 

    except Exception as e:
        logger.error(f'Unable to get data for [{folder}][{fileName}]: {e}')
        return []

    return
