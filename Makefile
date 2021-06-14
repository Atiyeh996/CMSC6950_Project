all = output
#CC=gcc
#CFLAGS=-I.
#all: output
output: tidynamics.msd.py tidynamics.correlation.py
	python tidynamics.correlation.py tidynamics.msd.py
#	$(CC) -o output tidynamics.msd.o $(CFLAGS)
tidynamics.correlation.py: 
	python tidynamics.correlation.py

tidynamics.msd.py:
	python tidynamics.msd.py
#clean:
#	rm *.png outpu
