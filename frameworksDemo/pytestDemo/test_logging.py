# __name__is to get to know that from which Tc logging is taking place
# logger object will be created with the help of getLogger()
# addHandler method is used to, when logger is asking me  in which file it should be saved and in which format,
# out object should know the place where our file has been located, this addHandler will accept another object that is filehandler
# fileHandler is an object where exactly the logs to be created.
# asctime is an variable when we run the file time will be printed.
# we are separating it by colon so i m mentioning it with : and s is to make it as string

import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("a debug statement is executed")
    logger.info("to print information statements")
    logger.warning("something is in warning mode")
    logger.error("a major error happened")
    logger.critical("critical issue")
