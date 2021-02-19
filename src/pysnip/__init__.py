import logging

logger = logging.getLogger(__name__)  # XXX
logger.setLevel(logging.DEBUG)
logging.basicConfig()

from .write_source import *
