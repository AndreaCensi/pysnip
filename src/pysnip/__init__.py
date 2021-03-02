__version__ = "7.1.2103021139"
__date__ = "2021-03-02T11:39:03.001947"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
