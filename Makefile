all = report.pdf
#CC=gcc
#CFLAGS=-I.
#all: output
report.pdf: tidynamics.correlation.py tidynamics.msd.py 
	python report.pdf tidynamics.correlation.py tidynamics.msd.py
#	$(CC) -o output tidynamics.msd.o $(CFLAGS)
tidynamics.correlation.py: visualization.tidynamics.correlation.py computational.tidynamics.correlation.py
	python tidynamics.correlation.py visualization.tidynamics.correlation.py computational.tidynamics.correlation.py

tidynamics.msd.py: visualization.tidynamics.msd.py computational.tidynamics.msd.py
	python tidynamics.msd.py visualization.tidynamics.msd.py computational.tidynamics.msd.py
#clean:
#	rm *.png outpu
