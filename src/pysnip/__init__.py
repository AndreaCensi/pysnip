__version__ = "7.1.2103061520"
__date__ = "2021-03-06T15:20:11.850775"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
