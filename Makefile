
PY=PYTHONPATH=src python
PDF_NAME="Haris_Gusic_Gauss_LLN_CLT.pdf"

.PHONY: all img src presentation

all: img src pdf

pdf:
	mkdir -p _build/
	@function ltx { \
		pdflatex -interaction=nonstopmode -output-directory _build/ main; \
	}; \
	ltx && bibtex _build/main && ltx && ltx
	mv _build/main.pdf _build/$(PDF_NAME)

img-gauss:
	mkdir -p _build/img/
	$(PY) scripts/gauss-uni.py
	$(PY) scripts/gauss-multi.py

img-lln:
	mkdir -p _build/img/
	$(PY) scripts/lln-demo.py
	$(PY) scripts/lln-hist.py

img-clt:
	mkdir -p _build/img/
	$(PY) scripts/clt-binom.py
	$(PY) scripts/clt-conv.py
	$(PY) scripts/clt-degen.py

img: img-gauss img-lln img-clt

src:
	mkdir -p _build/src
	cd src/; ../scripts/split-file.sh src/shared.py ../_build/src
	cd src/; ../scripts/split-file.sh src/gauss.py ../_build/src
	cd src/; ../scripts/split-file.sh src/lln.py ../_build/src
	cd src/; ../scripts/split-file.sh src/clt.py ../_build/src

presentation:
	cd presentation/ && $(MAKE)

zip: all zip-only

zip-only:
	rm -f HarisGusic_SIS2_Seminarski.zip
	zip -r HarisGusic_SIS2_Seminarski.zip main.tex literature.bib IEEEtranETF.bst \
		Makefile contents/ scripts/ src/*.py src/*.ipynb  \
		_build/img/ _build/main.pdf _build/src/

clean-img:
	rm -rf _build/img/

clean: 
	rm -rf _build/
