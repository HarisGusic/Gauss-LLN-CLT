
PY=PYTHONPATH=src python

.PHONY: img

all: img pdf

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

img: img-gauss img-lln img-clt

clean-img:
	rm -rf _build/img/

clean: clean-img
	rm -rf _build/
