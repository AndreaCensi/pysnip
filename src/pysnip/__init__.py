__version__ = "7.1.2104241742"
__date__ = "2021-04-24T17:42:02.590922"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
