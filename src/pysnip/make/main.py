from ..utils import CmdOptionParser
from . import pysnip_make
import sys

def pysnip_make_main():
    parser = CmdOptionParser('pysnip-make')

    parser.add_option("-d", dest='snippets_dir', default='snippets',
                      help="Directory containing snippets.")

    parser.add_option("-c", "--command", default=None,
                      help="Compmake command")

    options = parser.parse_options()

    res = pysnip_make(options.snippets_dir, options.command)
    
    sys.exit(res)


if __name__ == '__main__':
    pysnip_make_main()
