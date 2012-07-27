
install: install-python install-sty

install-python:
	python setup.py develop

TEXMFLOCAL=$(shell kpsewhich  -var-value TEXMFLOCAL)
dir=$(TEXMFLOCAL)/tex/latex/pysnip/
dest=$(dir)/pysnip.sty
src=$(CURDIR)/latex/pysnip.sty

install-sty:
	rm -f $(dest)
	mkdir -p $(dir)
	ln -s $(src) $(dest)
	mktexlsr   
