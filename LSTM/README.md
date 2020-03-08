# LSTM
Sentinel Healthcare LSTM Notebook

This LSTM model is built on top of the Keras deep learning library, using a Tensorflow backend, in a working SciPy environment. 

Jupyter Notebooks does simply function by importing these libraries inline. Instead, instantiate a virtual environment with the dependencies installed, then run Jupyter Notebooks from there and import as usual.

Prerequisite:

[VirtualEnv](https://pypi.org/project/virtualenv/)

Then, to configure your system for this Notebook, from your terminal enter:

```
virtualenv mylstm

source mylstm/bin/activate

pip3 install jupyter

pip3 install keras

python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose

pip3 install tensorflow

pip install -U scikit-learn

pip install statsmodels

jupyter notebook
```

From Jupyter Notebooks in your browser, navigate to your local/clone of this repo and run mylstm.ipynb.
