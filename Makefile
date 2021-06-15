#out.pdf: figure.msd.png figure.correlation.png
#	python figure.msd.png -i  figure.correlation.png -o out.pdf

#figure.msd: computational.tidynamics.msd.py visualization.tidynamics.msd.py
figure_msd.png: tidynamics.msd.py
	python tidynamics.msd.py figure_msd.png

#figure.correlation: computational.tidynamics.correlation.py visualization.tidynamics.correlation.py
figure_correlation.png: tidynamics.correlation.py
	python tidynamics.correlation.py figure_correlation.png

out.pdf: figure_msd.png figure_correlation.png
	python figure_msd.png -i figure_correlation.png -o out.pdf
