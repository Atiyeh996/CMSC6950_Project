default: report.pdf
.PHONY : default
report.pdf: report.tex msd.png acf1.png Memorial-University-of-Newfoundland5.jpeg  bibliography.bib 
	latexmk -pdf

msd.png: visualization.tidynamics.msd.py Data.csv
	python visualization.tidynamics.msd.py Data.csv msd.png

acf1.png: visualization.tidynamics.acf.py acf1.csv time.txt time2.txt
	python visualization.tidynamics.acf.py acf1.csv time.txt time2.txt acf1.png

Memorial-University-of-Newfoundland5.jpeg: Memorial-University-of-Newfoundland5.jpeg
	wget https://www.docspal.com/files/processed/72/18560772-sywxqhhs/Memorial-University-of-Newfoundland5.jpeg

Data.csv: computational.tidynamics.msd.py
	python computational.tidynamics.msd.py Data.csv

acf1.csv: computational.tidynamics.acf.py numbers1.txt
	python computational.tidynamics.acf.py numbers1.txt acf1.csv

time.txt: time.txt
	wget https://www.docspal.com/files/processed/01/18560701-pgehseam/time.txt

time2.txt: time2.txt
	wget https://www.docspal.com/files/processed/08/18560708-lltlbwfs/time2.txt

numbers1.txt: numbers1.txt
	wget https://www.docspal.com/files/processed/80/18560680-vecgenuf/numbers1.txt






clean:
	rm *.pdf
	rm *.log
	rm *.png
	rm *.aux
	rm *.fls
	rm Memorial-University-of-Newfoundland5.jpeg
#	rm *.csv
	rm *.fdb_latexmk
	rm *.blg
	rm *.txt
#	rm *.csv
#	rm Memorial-University-of-Newfoundland5.jpeg
	rm *.bbl
	rm *.dvi
	
.PHONY : clean


