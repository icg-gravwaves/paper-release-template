MAIN = main

.PHONY: pdf clean

pdf:
	latexmk -pdf -bibtex -interaction=nonstopmode -file-line-error $(MAIN).tex

clean:
	latexmk -C $(MAIN).tex
	rm -f $(MAIN)Notes.bib $(MAIN).bbl
