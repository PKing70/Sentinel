# Sentinel LSTM Model

This LSTM model 

## How to Use

The LSTM model is access via the `LSTM.ipynb` Jupyter Notebook. The model is built using the Keras deep learning library on a Tensorflow backend, in a working SciPy environment.

Jupyter does not simply function by importing these libraries inline (Known issue)[]. Instead, you must instantiate a virtual environment with the dependencies installed, then run Jupyter Notebooks from the virtual environment. 

### Prerequisite

[VirtualEnv](https://pypi.org/project/virtualenv/)

Install VirtualEnv according to their instructions.

### Activate Virtual Environment

Once VirtualEnv is installed, to configure your system for this Notebook, from your terminal enter:

```
virtualenv lstm

source lstm/bin/activate

python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose keras tensorflow scikit-learn

jupyter notebook
```

### LSTM Jupyter Notebook

From Jupyter Notebooks in your browser, navigate to your local/clone of this repo and run lstm.ipynb.

When finished, quit Jupyter Notebooks, then from the terminal, deactivate your virtualenv:

```
deactivate
```

## Source data

This model assumes you have a copy of `vitals_combined_interpolated.csv` in your working directory. If you don't have this data, you likely don't have permission from Sentinel to access this customer medical data.
