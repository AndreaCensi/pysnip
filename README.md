pysnip
======

PySnip is a LaTeX package for executing Python snippets from LaTeX.
It is inspired by ``python.sty``, developed by James Brotchie, but it 
has a few differences.

The most important difference is that the snippets are run by an external program,
called ``pysnip-make`` rather than within the LaTeX interpreter. Parallel 
computation is supported by using [compmake](http://github.com/AndreaCensi/compmake).


See the PDF manual at:

  https://github.com/AndreaCensi/pysnip/blob/master/latex/pysnip-manual.pdf