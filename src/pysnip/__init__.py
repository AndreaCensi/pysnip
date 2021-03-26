__version__ = "7.1.2103262007"
__date__ = "2021-03-26T20:07:37.246784"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
