from . import logger
from ..utils import Capture
import os
import traceback

# States of computation:
#
#  not-started
NOTSTARTED = 0
##  failed, needs_update
#FAILED_NEEDSUPDATE = 1
##  failed, uptodate
#FAILED_UPTODATE = 2
FAILED = 2
#  done, needs_update
DONE_NEEDSUPDATE = 3
#  done, uptodate
DONE_UPTODATE = 4

allStatus = [NOTSTARTED, FAILED, DONE_NEEDSUPDATE, DONE_UPTODATE]

class Job():
    def __init__(self, dirname, basename):
        self.dirname = dirname
        self.basename = basename
        self.status = self.find_status()
        assert self.status in allStatus
        
    def find_status(self):
        self.rcfile = os.path.join(self.dirname, '%s.rc' % self.basename)
        self.texfile = os.path.join(self.dirname, '%s.tex' % self.basename)
        self.pyfile = os.path.join(self.dirname, '%s.py' % self.basename)
        self.pyofile = os.path.join(self.dirname, '%s.pyo' % self.basename)
     
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
    
        uptodate = (os.path.exists(self.pyofile) and 
                    (contents(self.pyofile) == contents(self.pyofile)))
        
        if uptodate:
            return DONE_UPTODATE
        else:
            return DONE_NEEDSUPDATE

    def run(self):
        pycode = contents(self.pyfile)
        
        pycode_compiled = compile(pycode, self.pyfile, 'exec')
                
        cap = Capture(prefix=self.basename, echo_stdout=False,
                      echo_stderr=True)
        
        try:
            with cap.go():
                eval(pycode_compiled)
                
            with open(self.texfile, 'w') as f:
                f.write(cap.get_logged_stdout())
                
            with open(self.pyofile, 'w') as f:
                f.write(pycode)
                
            with open(self.rcfile, 'w') as f:
                f.write("0\n")
                
        except Exception as e:
            logger.error('Failed running snippets %s' % self.basename)
            logger.error('Code:\n%s' % pycode)
            outfile = os.path.join(self.dirname, self.basename + '.tex.incomplete')
            with open(outfile, 'w') as f:
                f.write(cap.get_logged_stdout())
                
            errfile = os.path.join(self.dirname, self.basename + '.err')
            with open(errfile, 'w') as f: 
                f.write(cap.get_logged_stderr())
                f.write(traceback.format_exc(e))
            
            with open(self.rcfile, 'w') as f:
                f.write("1\n")
            
            raise 
            
      
 
def contents(f):
    return open(f).read().strip()
        
