all: pysnip-manual.pdf

%.pdf: %.tex
	mkdir -p snippets/
	pdflatex -shell-escape $*
	pysnip-make -c make
	pdflatex -shell-escape $*

clean:
	rm -f pysnip-manual.pdf
	rm -rf snippets/

texhome=$(shell kpsewhich -var-value=TEXMFLOCAL)

install:
	mkdir -p $(texhome)
	ln -s -f $(CURDIR)/pysnip.sty $(texhome)/tex/latex/local/pysnip.sty
	sudo texhash
	kpsewhich pysnip.sty
