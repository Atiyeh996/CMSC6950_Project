default: report.pdf
.PHONY : default
report.pdf: msd.png acf.png  report.tex bibliography.bib Data.csv time.csv time2.csv acf.csv numbers1.csv
	pdflatex report.tex

#figure_msd.png: tidynamics.msd.py
#	python tidynamics.msd.py



#tidynamics.msd.py: computational.tidynamics.msd.py visualization.tidynamics.msd.py
#	python computational.tidynamics.msd.py visualization.tidynamics.msd.py


#figure_correlation.png: tidynamics.correlation.py
#	python tidynamics.correlation.py


#tidynamics.correlation.py: computational.tidynamics.correlation.py visualization.tidynamics.correlation.py
#	python computational.tidynamics.correlation.py visualization.tidynamics.correlation.py





#clean:
#	rm *.pdf
#	rm *.log
#	rm *.png
#	rm *.aux
#	rm *.fls
#	rm *.dvi
#	rm *.fdb_latexmk


#.PHONY : clean


