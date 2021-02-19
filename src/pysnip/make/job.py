import os
import traceback

from . import logger
from ..utils import Capture

# States of computation:
#
#  not-started
NOTSTARTED = 0
##  failed, needs_update
# FAILED_NEEDSUPDATE = 1
##  failed, uptodate
# FAILED_UPTODATE = 2
FAILED = 2
#  done, needs_update
DONE_NEEDSUPDATE = 3
#  done, uptodate
DONE_UPTODATE = 4

allStatus = [NOTSTARTED, FAILED, DONE_NEEDSUPDATE, DONE_UPTODATE]


class Job:
    def __init__(self, dirname, basename):
        self.dirname = dirname
        self.basename = basename
        self.status = self.find_status()
        assert self.status in allStatus

    def find_status(self):
        self.rcfile = os.path.join(self.dirname, "%s.rc" % self.basename)
        self.texfile = os.path.join(self.dirname, "%s.tex" % self.basename)
        self.pyfile = os.path.join(self.dirname, "%s.py" % self.basename)
        self.pyofile = os.path.join(self.dirname, "%s.pyo" % self.basename)
        self.texincfile = os.path.join(self.dirname, "%s.tex.inc" % self.basename)
        self.errfile = os.path.join(self.dirname, "%s.err" % self.basename)

        assert os.path.exists(self.pyfile)
        if not os.path.exists(self.rcfile):
            return NOTSTARTED

        if not os.path.exists(self.texfile):
            return FAILED

        # If basename.rc exists but the value is nonzero,
        # make basename.py more recent than basename.tex
        # and return (forces redo)

        rcvalue = contents(self.rcfile)
        failed = rcvalue != "0"

        if failed:
            return FAILED

        # If basename.pyo exists and the content is the same
        # as basename.py; mark basename.tex more recent than basename.py
        # (prevents returns)

        uptodate = os.path.exists(self.pyofile) and (
            contents(self.pyofile) == contents(self.pyfile)
        )

        if uptodate:
            return DONE_UPTODATE
        else:
            return DONE_NEEDSUPDATE

    def run(self):
        pycode = contents(self.pyfile)

        pycode_compiled = compile(pycode, self.pyfile, "exec")

        cap = Capture(prefix=self.basename, echo_stdout=False, echo_stderr=True)

        try:
            with cap.go():
                eval(pycode_compiled)

            write_to_file(self.texfile, cap.get_logged_stdout())
            write_to_file(self.pyofile, pycode)
            write_to_file(self.rcfile, "0\n")

            delete_if_exists(self.texincfile)
            delete_if_exists(self.errfile)

        except Exception as e:
            logger.error("Failed running snippets %s" % self.basename)
            logger.error("Code:\n%s" % pycode)

            delete_if_exists(self.pyofile)
            delete_if_exists(self.texfile)

            write_to_file(self.texincfile, cap.get_logged_stdout())
            write_to_file(
                self.errfile, cap.get_logged_stderr() + "\n" + traceback.format_exc(e)
            )
            write_to_file(self.rcfile, "1\n")
            raise


def write_to_file(filename, what):
    with open(filename, "w") as f:
        f.write(what)


def delete_if_exists(x):
    if os.path.exists(x):
        os.unlink(x)


def contents(f):
    return open(f).read().strip()
