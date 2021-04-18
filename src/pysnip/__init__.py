__version__ = "7.1.2104181348"
__date__ = "2021-04-18T13:48:12.544401"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
