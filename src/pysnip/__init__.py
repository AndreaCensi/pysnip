__version__ = "7.1.2104242003"
__date__ = "2021-04-24T20:03:06.879134"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
