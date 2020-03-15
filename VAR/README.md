# Vector Autoregression (VAR)
### Sentinel Healthcare VAR Notebook

The VAR model is built using the statsmodels.tsa.api package.

### Prerequisite
Python 3.7.3

Numpy 1.16.2 https://pypi.org/project/numpy/1.16.2/

Pandas 0.24.2 https://pandas.pydata.org/pandas-docs/version/0.24.2/

Matplotlib 3.0.2 https://matplotlib.org/3.0.2/contents.html

Statsmodels 0.9.0 https://www.statsmodels.org/0.9.0/


Running the jupyter notebook VAR.ipynb will output 2 datasets:
| dataset name | description |
| :------------ |:------------| 
| flags_stats.csv | flags stats for VAR model |
| models_stats.csv | model stats for VAR model |

## Source data

This model assumes you have a copy of `vitals_combined_interpolated.csv` in your working directory. If you don't have this data, you likely don't have permission from Sentinel to access this customer medical data.



