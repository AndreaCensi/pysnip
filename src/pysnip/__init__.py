__version__ = "7.1.2105081717"
__date__ = "2021-05-08T17:17:25.307894+00:00"
from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .write_source import *
