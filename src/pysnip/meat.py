import os
from glob import glob
from typing import cast

from compmake import (
    Cache,
    CMJobID,
    Context,
    get_job_cache,
    job_exists,
    mark_as_failed,
    StorageFilesystem,
)
from compmake.actions import mark_as_done, mark_as_notstarted
from zuper_commons.fs import DirPath
from . import DONE_NEEDSUPDATE, DONE_UPTODATE, FAILED, Job, logger, NOTSTARTED


def run_job(job: Job) -> None:
    job.run()


def get_last_mtime(d: DirPath):
    files = glob(os.path.join(d, "*.py"))
    return max(os.stat(_).st_mtime for _ in files)


def pysnip_make(c: Context, db: StorageFilesystem, dirname: DirPath):
    files = glob(os.path.join(dirname, "**/*.py"))
    # prefixes = [os.path.splitext(os.path.basename(f))[0] for f in files]
    logger.info(f"Found {len(files)} snippets in directory {dirname}")

    # use_filesystem(os.path.join(dirname, ".compmake"))
    dirs = set()
    ntodo = 0
    for filename in files:
        d = os.path.dirname(filename)
        dirs.add(d)
        dtime = get_last_mtime(d)
        mtime = os.stat(filename).st_mtime
        delta = dtime - mtime
        if delta > 60:
            logger.warn("Is this an old file? deleting", fn=filename, delta=delta)
            os.unlink(filename)
            continue

        basename, _ = os.path.splitext(os.path.basename(filename))
        job = Job(dirname=d, basename=basename, filename=filename)
        job_id = cast(CMJobID, job.basename)
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

    for d in dirs:
        good_roots = set()
        for f in os.listdir(d):
            if f.endswith(".py"):
                basename, _, _ = f.partition(".")  # remove double extension
                good_roots.add(basename)

        for f in os.listdir(d):
            fn = os.path.join(d, f)

            if not os.path.isfile(fn):
                continue
            basename, _, ext = f.partition(".")  # remove double extension
            if ext not in ["texi", "rc", "err", "pyo"]:
                continue

            if not basename in good_roots:
                os.unlink(fn)
                logger.warn("deleted", fn=fn, good=good_roots)
