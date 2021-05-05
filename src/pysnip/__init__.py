__version__ = "7.1.2105051555"
__date__ = "2021-05-05T15:55:51.334750+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
