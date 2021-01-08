
PY=PYTHONPATH=src python

.PHONY: img

all: img pdf

pdf:
	mkdir -p _build/
	pdflatex -interaction=nonstopmode -output-directory _build main.tex 

img:
	mkdir -p _build/img/
	$(PY) scripts/gauss-uni.py
	$(PY) scripts/gauss-multi.py

clean-img:
	rm -rf _build/img/

clean: clean-img
	rm -rf _build/
