import logging

logging.basicConfig(filename='mylog.txt',level=logging.ERROR)
#logging.basicConfig(filename='mylog.txt',level=logging.WARNING)
#logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.error('There is an error in Program')
logging.critical('There is a critical error in Program')
logging.warning('There is a warning in Program')
logging.info('There is a info in Program')
logging.debug('There is a debug message in Program') 
