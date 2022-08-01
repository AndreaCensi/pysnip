import asyncio
import os

from compmake import ContextImp, StorageFilesystem
from zuper_commons.cmds import ExitCode
from zuper_utils_asyncio import MyAsyncExitStack
from zuper_zapp import zapp1, ZappEnv
from . import pysnip_make
from ..utils import CmdOptionParser


@zapp1()
async def pysnip_make_main(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    await sti.started_and_yield()

    parser = CmdOptionParser("pysnip-make")

    parser.add_option(
        "-d",
        dest="snippets_dir",
        default="snippets",
        help="Directory containing snippets.",
    )

    parser.add_option("-c", "--command", default=None, help="Compmake command")

    options = parser.parse_options()
    d = options.snippets_dir
    dirname = os.path.join(d, "compmake")
    db = StorageFilesystem(dirname, compress=True)

    async with MyAsyncExitStack(sti) as AES:
        context = await AES.init(ContextImp(db=db, name="pysnip"))

        pysnip_make(context, db, d)
        await asyncio.sleep(4)
        if options.command:
            return await context.batch_command(sti, options.command)
        else:
            await context.compmake_console(sti)
        return ExitCode.OK


#
# def pysnip_make_main():
#     parser = CmdOptionParser("pysnip-make")
#
#     parser.add_option(
#         "-d",
#         dest="snippets_dir",
#         default="snippets",
#         help="Directory containing snippets.",
#     )
#
#     parser.add_option("-c", "--command", default=None, help="Compmake command")
#
#     options = parser.parse_options()
#
#     res = pysnip_make(options.snippets_dir, options.command)
#
#     sys.exit(res)


if __name__ == "__main__":
    pysnip_make_main()
