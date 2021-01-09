
PY=PYTHONPATH=src python

.PHONY: img

all: img pdf

pdf:
	mkdir -p _build/
	pdflatex -interaction=nonstopmode -output-directory _build main.tex 

img-gauss:
	$(PY) scripts/gauss-uni.py
	$(PY) scripts/gauss-multi.py

img-clt:
	$(PY) scripts/clt-binom.py

img: img-gauss img-clt
	mkdir -p _build/img/

clean-img:
	rm -rf _build/img/

clean: clean-img
	rm -rf _build/
