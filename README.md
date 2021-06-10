# CMSC6950_Project
***Course project for CMSC6950 Spring 2021***

**Tidynamics : a tiny package to compute the dynamics of stochastic and molecular simulations**


**Atiyeh Tahavorgar**

## Software setup

It is necessary to have Python and NumPy to install and use tidynamics.

create conda environment in your project:

```
conda create -n <envname>
```

after installation, activation is necessary:

```
conda activate <envname>
```
install python and numpy within conda:

```
conda install python numpy
```

Tidynamics can be installed with pip:

```
pip install --user tidynamics
```

or with conda (preferred way):

```
conda install -c conda-forge tidynamics
```
after installation, you must test it in tidynamics directory:

```
python -m pytest
```
Installing tidynamics does not install the tests. It is necessary to download tidynamics' source and to install
pytest to run the tests.

you can use following codes to download tidynamics sourse and pytest:

```
git clone https://github.com/pdebuyl-lab/tidynamics
pip install pytest
```
