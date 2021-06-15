all: report.pdf
report.pdf: figure_msd.png figure_correlation.png
	cp figure_msd.png  figure_correlation.png > report.pdf

figure_msd.png: tidynamics.msd.py
	python tidynamics.msd.py > figure_msd.png

tidynamics.msd.py: computational.tidynamics.msd.py visualization.tidynamics.msd.py
	python computational.tidynamics.msd.py visualization.tidynamics.msd.py


figure_correlation.png: tidynamics.correlation.py
	python tidynamics.correlation.py

tidynamics.correlation.py: computational.tidynamics.correlation.py visualization.tidynamics.correlation.py
	python computational.tidynamics.correlation.py visualization.tidynamics.correlation.py

clean:
	rm *.png
	rm *.pdf

#.PHONY : clean

