from . import Job, DONE_UPTODATE, FAILED, DONE_NEEDSUPDATE, NOTSTARTED, logger
from compmake import comp, compmake_console, use_filesystem
from glob import glob
import os
from compmake.ui.console import batch_command
from compmake.jobs.actions import mark_as_done

def run_job(job):
    job.run()


def pysnip_make(dirname, compmake_command):
    files = glob(os.path.join(dirname, '*.py'))
    prefixes = [os.path.splitext(os.path.basename(f))[0] for f in files]
    logger.info('Found %d snippets in directory %s' % (len(prefixes), dirname))
    
    use_filesystem(os.path.join(dirname, '.compmake'))
    ntodo = 0
    for p in prefixes:
        job = Job(dirname, p)
        if job.status == DONE_UPTODATE:
            #logger.info('%s: done' % job.basename)
            pass
        elif job.status == FAILED:
            logger.info('%s: failed' % job.basename)
        elif job.status == DONE_NEEDSUPDATE:
            logger.info('%s: done (but needs update)' % job.basename)
            pass
        elif job.status == NOTSTARTED:
            #logger.info('%s: not started' % job.basename)
            pass
        
        job_id = job.basename
        comp(run_job, job, job_id=job_id) 
        if job.status == DONE_UPTODATE:
            mark_as_done(job_id)
        else:
            ntodo += 1
            
            
            

    logger.info('%d/%d jobs to do' % (ntodo, len(prefixes)))
    if compmake_command is not None:
        return batch_command(compmake_command)
    else:
        compmake_console()
        return 0
 
     
