__version__ = "7.1.2103012049"
__date__ = "2021-03-01T20:49:19.166261"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
