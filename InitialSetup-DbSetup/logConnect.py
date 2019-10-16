import logging


# Create and configure logger
def initializeLog(name):
    logging.basicConfig(filename=name,
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger
