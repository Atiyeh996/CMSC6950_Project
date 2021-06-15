#out.pdf: figure.msd.png figure.correlation.png
#	python figure.msd.png -i  figure.correlation.png -o out.pdf

#figure.msd: computational.tidynamics.msd.py visualization.tidynamics.msd.py
figure.msd.png: tidynamics.msd.py
	python tidynamics.msd.py > figure.msd.png

#figure.correlation: computational.tidynamics.correlation.py visualization.tidynamics.correlation.py
figure.correlation.png: tidynamics.correlation.py
	python tidynamics.correlation.py > figure.correlation.png

out.pdf: figure.msd.png figure.correlation.png
	python figure.msd.png -i  figure.correlation.png -o out.pdf
