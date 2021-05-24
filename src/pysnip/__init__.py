__version__ = "7.1.2105241926"
__date__ = "2021-05-24T19:26:08.798109+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
