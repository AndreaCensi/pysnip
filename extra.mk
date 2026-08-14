.PHONY: clean install install-python install-sty compile

clean:
	coverage erase
	rm -rf $(out) $(out)/coverage $(out)/test-results

install: install-python install-sty

install-python:
	python -m pip install --editable .

TEXMFLOCAL=$(shell kpsewhich -var-value TEXMFLOCAL)
dir=$(TEXMFLOCAL)/tex/latex/pysnip/
dest=$(dir)/pysnip.sty
src=$(CURDIR)/latex/pysnip.sty

install-sty:
	rm -f $(dest)
	mkdir -p $(dir)
	ln -s $(src) $(dest)
	mktexlsr

compile:
	pyinstaller --onefile --distpath . script.py
