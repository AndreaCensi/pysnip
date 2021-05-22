__version__ = "7.1.2105221948"
__date__ = "2021-05-22T19:48:17.075504+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
