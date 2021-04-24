__version__ = "7.1.2104241833"
__date__ = "2021-04-24T18:33:04.067005"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
