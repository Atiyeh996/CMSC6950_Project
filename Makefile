default: report.pdf
.PHONY : default
report.pdf: report.tex msd.png acf.png Memorial-University-of-Newfoundland5.png  bibliography.bib 
	latexmk -pdf

msd.png: visualization.tidynamics.msd.py Data.csv
	python visualization.tidynamics.msd.py Data.csv msd.png

acf.png: visualization.tidynamics.acf.py acf.csv time.csv time2.csv
	python visualization.tidynamics.acf.py acf.csv time.csv time2.csv acf.png

Data.csv: computational.tidynamics.msd.py 
	python computational.tidynamics.msd.py Data.csv

acf.csv: computational.tidynamics.acf.py numbers1.csv
	python computational.tidynamics.acf.py numbers1.csv acf.csv






#clean:
#	rm *.pdf
#	rm *.log
#	rm *.png
#	rm *.aux
#	rm *.fls
#	rm *.dvi
#	rm *.fdb_latexmk


#.PHONY : clean


