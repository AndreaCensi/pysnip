from compmake.jobs.actions import colorize_loglevel
from compmake.utils.capture import OutputCapture
from contextlib import contextmanager
import logging

      
class Capture:
    def __init__(self, prefix, echo_stdout=True, echo_stderr=True,
                 capture_logging=False):
        self.prefix = prefix
        self.echo_stdout = echo_stdout
        self.echo_stderr = echo_stderr
        self.capture_logging = capture_logging
    
    def start(self):
        self.capture = OutputCapture(prefix=self.prefix,
                                echo_stdout=self.echo_stdout,
                                echo_stderr=self.echo_stderr)

        # TODO: add whether we should just capture and not echo
        self.old_emit = logging.StreamHandler.emit
        
#        if self.capture_logging:
        def my_emit(_, log_record):
            msg = colorize_loglevel(log_record.levelno, log_record.msg)
            #  levelname = log_record.levelname
            name = log_record.name

            #print('%s:%s:%s' % (name, levelname, msg)) 
#                print('%s:%s' % (name, msg))
            self.capture.old_stderr.write('>%s:%s\n' % (name, msg))

        logging.StreamHandler.emit = my_emit
    
    @contextmanager
    def go(self):
        self.start()
        try:
            yield
        finally:
            self.stop()
    
    def stop(self):
        self.capture.deactivate() 
        logging.StreamHandler.emit = self.old_emit
        
    def get_logged_stderr(self):
        return self.capture.get_logged_stderr()
    
    def get_logged_stdout(self):
        return self.capture.get_logged_stdout()
    
