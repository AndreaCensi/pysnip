all: pysnip-manual.pdf

%.pdf: %.tex
	mkdir -p snippets/
	pdflatex $*
	pysnip-make -c make
	pdflatex $*

clean:
	rm pysnip-manual.pdf
	rm -rf snippets/