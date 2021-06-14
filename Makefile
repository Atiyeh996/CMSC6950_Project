target : report.pdf

report.pdf : tidynamics.correlation.py tidynamics.msd.py
	python report.pdf tidynamics.correlation.py tidynamics.msd.py
