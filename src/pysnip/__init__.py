__version__ = "7.1.2105221639"
__date__ = "2021-05-22T16:39:33.178453+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
