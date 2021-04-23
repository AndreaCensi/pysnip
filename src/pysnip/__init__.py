__version__ = "7.1.2104231703"
__date__ = "2021-04-23T17:03:35.209606"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
