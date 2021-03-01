import os
from glob import glob

from compmake import Cache, Context, get_job_cache, job_exists, mark_as_failed, StorageFilesystem
from compmake.actions import mark_as_done, mark_as_notstarted
from zuper_commons.fs import DirPath
from . import DONE_NEEDSUPDATE, DONE_UPTODATE, FAILED, Job, logger, NOTSTARTED


def run_job(job: Job) -> None:
    job.run()


def pysnip_make(c: Context, db: StorageFilesystem, dirname: DirPath):
    files = glob(os.path.join(dirname, "**/*.py"))
    # prefixes = [os.path.splitext(os.path.basename(f))[0] for f in files]
    logger.info("Found %d snippets in directory %s" % (len(files), dirname))

    # use_filesystem(os.path.join(dirname, ".compmake"))
    ntodo = 0
    for filename in files:
        d = os.path.dirname(filename)
        basename, _ = os.path.splitext(os.path.basename(filename))
        job = Job(dirname=d, basename=basename, filename=filename)
        job_id = job.basename
        current_state = None
        if job_exists(job_id, db):
            current_state = get_job_cache(job_id, db).state

        if job.status == DONE_UPTODATE:
            #            logger.info('%s: done' % job.basename)
            if current_state != Cache.DONE:
                mark_as_done(job_id, db, None)
            pass
        elif job.status == FAILED:
            #            logger.info('%s: failed' % job.basename)
            if current_state != Cache.FAILED:
                mark_as_failed(job_id, db)
        elif job.status == DONE_NEEDSUPDATE:
            mark_as_notstarted(job_id, db)
            #            logger.info('%s: done (but needs update)' % job.basename)
            pass
        elif job.status == NOTSTARTED:
            mark_as_notstarted(job_id, db)
            #            logger.info('%s: not started' % job.basename)
            pass
        c.comp(run_job, job, job_id=job_id)
        if job.status != DONE_UPTODATE:
            ntodo += 1
