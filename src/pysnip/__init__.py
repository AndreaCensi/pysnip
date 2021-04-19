__version__ = "7.1.2104191743"
__date__ = "2021-04-19T17:43:17.115208"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
