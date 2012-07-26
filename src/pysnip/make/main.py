from ..utils import CmdOptionParser
from . import pysnip_make

def pysnip_make_main():
    parser = CmdOptionParser('pysnip-make')

    parser.add_option("-d", dest='snippets_dir', default='snippets',
                      help="Directory containing snippets.")

    parser.add_option("-c", "--command", default=None,
                      help="Compmake command")

    options = parser.parse_options()

    pysnip_make(options.snippets_dir, options.command)
    


if __name__ == '__main__':
    pysnip_make_main()
