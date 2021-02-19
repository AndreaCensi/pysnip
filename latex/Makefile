all: pysnip-manual.pdf

%.pdf: %.tex
	mkdir -p snippets/
	pdflatex -shell-escape $*
	pysnip-make -c make
	pdflatex -shell-escape $*

clean:
	rm -f pysnip-manual.pdf
	rm -rf snippets/
