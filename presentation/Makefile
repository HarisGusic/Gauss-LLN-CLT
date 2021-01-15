
PRESENTATION_NAME=Presentation_Gauss-LLN-CLT.pdf
THEME_SRC=theme/source

.PHONY: theme

all: theme
	mkdir -p ../_build/
	pdflatex -interaction=nonstopmode -output-directory=../_build presentation.tex
	cd ../_build/; mv presentation.pdf "$(PRESENTATION_NAME)"

theme:
	mkdir -p $(THEME_SRC)/_build/
	cd $(THEME_SRC) && \
		latex -interaction=nonstopmode -output-directory=_build \
		beamerthememetropolis.ins

clean:
	rm -rf $(THEME_SRC)/_build
	rm -rf _build/
	rm -f ../_build/"$(PRESENTATION_NAME)"
