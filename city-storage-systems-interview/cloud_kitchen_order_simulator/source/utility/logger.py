import logging
from logdecorator import log_on_start

mesage_format = '%(asctime)-15s %(user)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG)