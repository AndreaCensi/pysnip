__version__ = "7.1.2105061655"
__date__ = "2021-05-06T16:55:30.515826+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
