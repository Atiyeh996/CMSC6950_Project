#!/usr/bin/env python
"""
====================================
Command-line interface to tidynamics
====================================

The program reads in data from the file input_file (using np.loadtxt from
NumPy) and performs the selected action on the data, chosen in:

* acf for the autocorrelation function
* msd for the mean-square displacement

The program writes the result in the file output_file using the function
np.savetxt from NumPy.

For more information, consult the documentation of tidynamics at
http://lab.pdebuyl.be/tidynamics/

"""
from __future__ import print_function, division
import sys
import argparse
import numpy as np
import tidynamics
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__,
                        formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('action',
                    help='Choice of computation to perform on input file',
                    choices=['acf', 'msd'])
parser.add_argument('input_file',
                    help='Filename for input data')
parser.add_argument('output_file',
                    help='Filename for the result of the computation')
args = parser.parse_args()

#input_data = np.loadtxt("msd","acf")
input_data = np.loadtxt(args.input_file)

if args.action == 'acf':
    result = tidynamics.acf(input_data)
   # result = tidynamics.acf("random_steps_sample_0.txt.gz")
elif args.action == 'msd':
    result = tidynamics.acf(input_data)
   # result = tidynamics.msd("random_steps_sample_0.txt.gz")


#plt.savefig('plot1.png', dpi=300, bbox_inches='tight')


#plt.show()
#np.savetxt(args.output_file, result)
np.loadtxt(args.output_file, result)
#plt.plot(file)
