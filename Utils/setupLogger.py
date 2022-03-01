import logging


def setupLogger(loggerName, logFile, logLevel=logging.INFO):
	"""Function setup loggers as many as possible"""
	formatter 		= logging.Formatter('[%(asctime)s] -- [%(levelname)s] -- %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
	
	# create logger
	logger	= logging.getLogger(loggerName)
	logger.setLevel(logLevel)

	# create file handler which logs even debug messages
	handler	= logging.FileHandler(logFile, mode='a')
	handler.setLevel(logging.DEBUG)
	
	# set formatter with handler
	handler.setFormatter(formatter)
	
	# add the handlers to the logger
	logger.addHandler(handler)
	
	# return the logger
	return logger

def readLogger():
	pass
