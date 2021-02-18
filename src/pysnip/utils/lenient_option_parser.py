from . import UserError
from optparse import IndentedHelpFormatter
import optparse
import sys


class LenientOptionParser(optparse.OptionParser):
    def parse_args(self, args):
        self.arguments = list(args)
        return optparse.OptionParser.parse_args(self, args)

    def error(self, msg):
        # msg = '%s: %s' % (self.get_prog_name(), msg)
        msg += "\nArguments: %s %s" % (self.get_prog_name(), " ".join(self.arguments))
        raise UserError(msg)


def MyOptionParser(prog, usage):
    formatter = IndentedHelpFormatter(
        indent_increment=2, max_help_position=80, width=100, short_first=1
    )

    parser = LenientOptionParser(prog=prog, formatter=formatter, usage=usage)
    parser.disable_interspersed_args()
    return parser


class CmdOptionParser(LenientOptionParser):
    def __init__(self, prog, usage=None, args=None):
        if args is None:
            args = sys.argv[1:]
        self.given = args

        formatter = IndentedHelpFormatter(
            indent_increment=2, max_help_position=80, width=100, short_first=1
        )

        LenientOptionParser.__init__(self, prog=prog, usage=usage, formatter=formatter)
        self.disable_interspersed_args()

    def parse(self):
        return self.parse_args(self.given)

    def parse_options(self):
        """ Returns only the options, checking no spurious args """
        options, args = self.parse()
        if args:
            raise UserError("Spurious arguments: %s" % args)
        return options
