# Sentinel

Sentinel Healthcare provides a remote management platform for clinicians and hospitals to monitor patient health and provide outreach. Patients regularly record vital signs with monitoring devices for analysis by Sentinel. 

The UW capstone team has developed prediction models for based on Sentinel’s vital signs, medication, and clinical notes data to improve health deterioration detection.


## Install and use

[Clone](https://help.github.com/en/articles/cloning-a-repository) this repository, or choose Download ZIP.

Then from your local copy, refer to the README for any model for specific information required to run that model.

## Data

The source for this data analysis were provided to the UW capstone team directly from Sentinel Healthcare, after anonymization. As a further privacy precaution, the data sources have not been made available in this repository.

The data dictionary for the provided data is as follows:

Vitals

**Column**|**Description**|**Type**|**Example**
:-----:|:-----:|:-----:|:-----:
created|Row creation timestamp|String|2019-11-03 15:53:57
"eventTypeAndTimestamp"|"Encoding for medicalevent"|String|MOBILEHEALTHDATA-1572764400000
patient\_uuid|Patient key|Integer|9988948
timestamp|Medical event timestamp|String|2019-11-03 0:00:00
updated|Row update timestamp|String|2019-11-03 15:53:57
DBP|Diastolic blood pressure|Float|70
DistanceTravel|Measurement of ambulatory movement (in what units? Km?)|Float|1.96313529
FAST|Whether patient is fasting|Boolean|TRUE
FASTVAL|Fasting value (?)|Boolean|TRUE
HR|Heart rate|Float|78
LBS|Weight in pounds|Float|168
PI|Perfusion index|Float|11
SBP|Systolic blood pressure|Float|127
SPO2|Peripheral capillary oxygen saturation|Float|97
Steps|Steps measured by device|Float|2189
TimeAwake|Measured awake time (units?)|Float|1561809251968
TimeInBed|Measured resting time|Float|1561777600077
TimeSleep|Measured sleeping time|Float|0
device|Type of measuring device|String|iHealth Track
deviceId|Identifier of device|String|F0B5D1A571E2
deviceModel|Model of device|String|KN\_550BT
deviceVendor|Maker of device|String|MocaCuff
height|Patient height (inches)|Float|66
identifier|TBD (?)|String|HealthKit
location|Where event occurs|String|office

Notes

**Column**|**Description**|**Type**|**Example**
:-----:|:-----:|:-----:|:-----:
created|Row creation timestamp|String|2019-11-03 15:53:57
"eventTypeAndTimestamp"|"Encoding for noteevent"|String|NOTE-1539909021000
note|Note written by Sentinel Healthcare staff|String|{'type': 'internal', 'content': 'CFC week 28'}
patient\_uuid|Patient key|Integer|9988948
timestamp|Medical event timestamp|String|2019-11-03 0:00:00
timezoneOffset|Offset value for timestamp|Integer|-300
updated|Row update timestamp|String|2019-11-03 15:53:57

## Software dependencies and license information

### Programming language

- [Python](https://www.python.org/downloads/) version 3.6 or above

#### Python packages needed

- [IPython](https://ipython.org/)
- [Jupyter](https://jupyter.org/)
- [Keras](https://keras.io/)
- [math](https://docs.python.org/3/library/math.html)
- [Matplotlib](https://matplotlib.org/)
- [nose](https://pypi.org/project/nose/)
- [NumPy](https://www.numpy.org)
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org)
- [scipy](https://www.scipy.org/)
- [statsmodels](https://www.statsmodels.org/)
- [SymPy](https://www.sympy.org/)
- [TensorFlow](https://www.tensorflow.org/)

#### License information

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). As a permissive license, it puts only very limited restriction on reuse and has therefore an excellent license compatibility. For detailed description of the contents of license please refer to the file [LICENSE](https://github.com/PKing70/LIMEaid/blob/master/LICENSE).

## Directory structure

Sentinel is organized as follows:

```sh

Sentinel (master)
|     LICENSE
|     README.md
|
|----- docs 
|     |      Sentinel Paper.pdf
|     |      SentinelPoster.pdf
|
|----- ARIMA
|     |     vitals_etl_explore_different_cosinor_models.ipynb
|     |     vitals_etl_explore_cosinor_interpolation_with_charts.ipynb
|     |     vitals_etl_cosinor_interpolation_newdata_HR_multicore.ipynb
|     |     vitals_etl_cosinor_interpolation_newdata_SBP_multicore.ipynb
|     |     vitals_combine_the_two_interpolated_datasets.ipynb
|     |     sarima_exploratory_work_with_charts.ipynb
|     |     sarima_prediction_and_forecast_hr.ipynb
|     |     sarima_prediction_and_forecast_sbp.ipynb
|     |     generate_sarima_flags.ipynb
|     |     generate_sarima_metrics.ipynb
|     |     sarima_flags_stats.csv
|     |     sarima_models_stats.csv
|     |     README.md
|
|----- LSTM
|     |     df_flags_lstm.csv
|     |     df_lstm_metrics.csv
|     |     df_model_lstm.csv
|     |     LSTM.ipynb
|     |     README.md
|
|----- VAR
|     |     flag_stats.csv
|     |     models_stats.csv
|     |     README.md
|     |     VAR.ipynb
|
|----- Chart
|     |     dataframe.js
|     |     dataframe.min.js
|     |     index.html
|     |     README.md
|     |     script.js
|     |     style.css

```

## Team members

* [Suman Bhagavathula](mailto:sumanbh@uw.edu)

* [Patrick King](mailto:pking70@uw.edu)

* [Agustin Lew](mailto:ablew@uw.edu)

* [Ankit Tandon](mailto:antand@uw.edu)
