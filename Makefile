bachelor:
	xelatex --synctex=1 main.tex
	-bibtex  main.aux
	xelatex --synctex=1 main.tex
	xelatex --synctex=1 main.tex

clean:
	find . -name '*.aux' -print0 | xargs -0 rm -rf
	rm -rf *.lof *.log *.lot *.out *.toc *.bbl *.blg *.thm  auto/ *.synctex.gz

depclean: clean
	rm -rf *.pdf
