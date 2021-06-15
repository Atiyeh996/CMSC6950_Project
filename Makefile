#all: report.pdf
figure_msd.png: tidynamics.msd.py
#figure_msd.png: tidynamics.msd.py
	python tidynamics.msd.py >  figure_msd.png

figure_correlation.png: tidynamics.correlation.py
	python tidynamics.correlation.py >  figure_msd.png


#figure_correlation.png: tidynamics.correlation.py
#	python tidynamics.correlation.py > figure_correlation.png


report.pdf: figure_msd.png figure_correlation.png
	cp figure_msd.png  figure_correlation.png > report.pdf


tiidynamics.msd.py: visualization.tidynamics.msd.py  computational.tidynamics.msd.py
	python tidynamics.msd.py

tidynamics.correlation.py: visualization.tidynamics.correlation.py  computational.tidynamics.correlation.py
	python tidynamics.correlation.py












#	mv figure_correlation.png > report.pdf
#	print("well done")

clean: 
	rm *.pdf
	rm *.png
