from . import Job, DONE_UPTODATE, FAILED, DONE_NEEDSUPDATE, NOTSTARTED, logger
from compmake import comp, compmake_console, use_filesystem, batch_command
from compmake.jobs import (get_job_cache, Cache, mark_as_done, mark_as_failed,
    mark_as_notstarted)
from glob import glob
import os

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
        job_id = job.basename
        if job.status == DONE_UPTODATE:
#            logger.info('%s: done' % job.basename)
            cache = get_job_cache(job_id)
            if not cache.state == Cache.DONE:
                mark_as_done(job_id)
            pass
        elif job.status == FAILED:
#            logger.info('%s: failed' % job.basename)
            mark_as_failed(job_id)
        elif job.status == DONE_NEEDSUPDATE:
            mark_as_notstarted(job_id)
#            logger.info('%s: done (but needs update)' % job.basename)
            pass
        elif job.status == NOTSTARTED:
            mark_as_notstarted(job_id)
#            logger.info('%s: not started' % job.basename)
            pass
        comp(run_job, job, job_id=job_id) 
        if job.status != DONE_UPTODATE:
            ntodo += 1
            
#    logger.info('%d/%d jobs to do' % (ntodo, len(prefixes)))
    batch_command('stats')
    if compmake_command is not None:
        return batch_command(compmake_command)
    else:
        compmake_console()
        return 0
 
     
