__version__ = "7.1.2107171706"
__date__ = "2021-07-17T17:06:03.603527+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
