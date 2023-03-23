import inspect
import textwrap


class MyClass:
    def f(self):
        a = 2
        a = 2


def write_source(m):
    s = inspect.getsource(m)
    s = textwrap.dedent(s)
    s = s.strip()
    print("\\begin{verbatim}")
    print(s)
    print("\\end{verbatim}%")


def write_source_minted(m, nodec: bool = False):
    s = inspect.getsource(m)
    s = textwrap.dedent(s)
    s = s.strip()

    if nodec:
        lines = s.split("\n")
        lines = [_ for _ in lines if not _.strip().startswith("@")]
        s = "\n".join(lines)
    # if 'PYSNIP_DRAFT' in os.environ:
    #     print('\\begin{verbatim}')
    #     print(s)
    #     print('\\end{verbatim}%')
    # else:
    print("\\begin{minted}[mathescape]{python}")
    print(s)
    print("\\end{minted}", end="")
