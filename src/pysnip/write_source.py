import inspect
import os


class MyClass:
    def f(self):
        a = 2
        a = 2

def write_source(m):

    s = inspect.getsource(m)
    print('\\begin{verbatim}')
    print(s)
    print('\\end{verbatim}')

def write_source_minted(m):
    s = inspect.getsource(m)
    if 'PYSNIP_DRAFT' in os.environ:
        print('\\begin{verbatim}')
        print(s)
        print('\\end{verbatim}')
    else:
        print('\\begin{minted}{python}')
        print(s)
        print('\\end{minted}')
