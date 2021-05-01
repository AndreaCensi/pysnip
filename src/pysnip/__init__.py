__version__ = "7.1.2105010823"
__date__ = "2021-05-01T08:23:39.644611+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
