default: report.pdf
.PHONY : default
report.pdf:report.tex bibliography.bib figure_correlation.png figure_msd.png
	pdflatex report.tex


figure_correlation.png: tidynamics.correlation.py
	python tidynamics.correlation.py


tidynamics.correlation.py: computational.tidynamics.correlation.py visualization.tidynamics.correlation.py
	python computational.tidynamics.correlation.py visualization.tidynamics.correlation.py


figure_msd.png: tidynamics.msd.py
	python tidynamics.msd.py


tidynamics.msd.py: computational.tidynamics.msd.py visualization.tidynamics.msd.py
	python computational.tidynamics.msd.py visualization.tidynamics.msd.py


clean:
	rm *.pdf
	rm *.log
	rm *.png
	rm *.aux
#	rm *.fls
	rm *.dvi
	rm *.fdb_latexmk


.PHONY : clean

