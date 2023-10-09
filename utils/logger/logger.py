import datetime
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)

# file path
timestamp = datetime.datetime.now()
file_handle = logging.FileHandler(f"utils/logger/logs/logs_{timestamp}.log")
# file_handle.setLevel(logging.INFO)
logger.addHandler(file_handle)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')