__version__ = "7.1.2105161225"
__date__ = "2021-05-16T12:25:32.321381+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
