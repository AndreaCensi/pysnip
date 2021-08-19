__version__ = "devel"
__date__ = "2021-08-11T13:29:21.087789+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
