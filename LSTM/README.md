# LSTM
Sentinel Healthcare LSTM Notebook

This LSTM model is built on top of the Keras deep learning library, using a Tensorflow backend, in a working SciPy environment. 

Jupyter Notebooks does simply function by importing these libraries inline. Instead, instantiate a virtual environment with the dependencies installed, then run Jupyter Notebooks from there and import as usual. For steps, follow below.

Prerequisite:

[VirtualEnv](https://pypi.org/project/virtualenv/)

To configure your system for this Notebook, from your terminal enter:

```
virtualenv lstm

source lstm/bin/activate

python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose keras tensorflow scikit-learn

jupyter notebook
```

From Jupyter Notebooks in your browser, navigate to your local/clone of this repo and run mylstm.ipynb.

When finished, quit Jupyter Notebooks, then from the terminal, deactivate your virtualenv:

```
deactivate
```
