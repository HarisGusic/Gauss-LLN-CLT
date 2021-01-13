
PY=PYTHONPATH=src python

.PHONY: img src

all: img src pdf

pdf:
	mkdir -p _build/
	pdflatex -interaction=nonstopmode -output-directory _build main.tex 

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
	cd src/; ../scripts/split-file.sh src/gauss.py ../_build/src
	cd src/; ../scripts/split-file.sh src/lln.py ../_build/src
	cd src/; ../scripts/split-file.sh src/clt.py ../_build/src

clean-img:
	rm -rf _build/img/

clean: clean-img
	rm -rf _build/

zip: all zip-only

zip-only:
	rm -f HarisGusic_SIS2_Sem.zip
	zip -r HarisGusic_SIS2_Sem.zip main.tex Makefile scripts/ src/ _build/img/ \
	_build/main.pdf
