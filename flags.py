"""
Functions for evaluationg

flags(df, report=False)
# df must be a 30-day time-series of the latest current data.
# df_train[-23:] combined with df_test or df_pred

compare_flags(df_train, df_test, df_pred)


accuracy_f1(true_positive, true_negative, false_positive, false_negative)
"""

import numpy as np
import pandas as pd


def flags(df, report=False):
    """
    Flag-raising algorithm based on health deterioration rules.

    df    : 30-day timeseries pandas dataframe.
    report: True if written report requested. False if status of each flag is wanted.

    output: returns a list containing the average value of HR and SBP during the last ten days of the time series,
            and the different flags that are raised based on the conditions above.
    """
    rising_HR = False
    lowering_HR = False
    rising_SBP = False
    high_BP = False

    first_ten = np.mean(df[:10])
    last_ten = np.mean(df[-10:])

    deltas = (last_ten - first_ten)

    if deltas[0] >= 10:
        rising_HR = True
        flag_message_1 = 'Detected rising heart rate. \n'
    elif deltas[0] <= -10:
        lowering_HR = True
        flag_message_1 = 'Detected decreasing heart rate. \n'
    else:
        flag_message_1 = 'No changes in heart rate detected. \n'

    if deltas[1] >= 5:
        rising_SBP = True
        flag_message_2 = 'Detected rising blood pressure (SBP). \n'
    else:
        flag_message_2 = 'No changes in blood pressure detected. \n'

    min_HR = np.sum(df.HR < 55)
    max_HR = np.sum(df.HR > 100)

    min_SBP = np.sum(df.SBP < 90)
    max_SBP = np.sum(df.SBP > 180)

    flag_message_3 = 'Heart rate lower than 55 bpm detected ' + str(min_HR) + ' times. \n'
    flag_message_4 = 'Heart rate greater than 100 bpm detected ' + str(max_HR) + ' times. \n'
    flag_message_5 = 'Systolic blood pressure (SBP) lower than 90 bpm detected ' + str(min_SBP) + ' times. \n'
    flag_message_6 = 'Systolic blood pressure (SBP) greater than 180 bpm detected ' + str(max_SBP) + ' times. \n'
    flag_message_7 = ''

    high_SBP = (df.SBP > 140) & (df.SBP < 179)

    if np.sum(high_SBP[-15:]) > 7:
        high_BP = True
        flag_message_7 = 'High blood pressure detected.'
    if report == True:
        if high_BP == True:
            message = flag_message_1 + flag_message_2 + flag_message_3 + flag_message_4 + flag_message_5 + flag_message_6 + flag_message_7 
        else:
            message = flag_message_1 + flag_message_2 + flag_message_3 + flag_message_4 + flag_message_5 + flag_message_6
        print(message)
    else:
        return [last_ten, rising_HR, lowering_HR, rising_SBP, min_HR, max_HR, min_SBP, max_SBP, high_BP]


def compare_flags(df_train, df_test, df_forecast):
    """
    CompaBres the results of the flag-raising algorithm.

    df_train   : training set of the timeseries for a particular patient.
    df_test    : test set of the timeseries for a particular patient.
    df_forecast: forecast of the timeseries for a particular patient.

    output     : list containing HR_error, SBP_error, algorithm accuracy, 
                 predicted flags and actual flags.
    """
    flag_comparison = []
    current = df_train[['HR','SBP']][-23:].copy()
    future = df_test[['HR','SBP']].copy()
    forecast = df_forecast.copy()
    forecast.columns = ['HR', 'SBP']
    actual = pd.concat([current, future])
    pred = pd.concat([current, forecast])

    actual_flags = flags(actual)
    pred_flags = flags(pred)

    HR_error = np.abs(pred_flags[0][0] - actual_flags[0][0]) / actual_flags[0][0]
    SBP_error = np.abs(pred_flags[0][1] - actual_flags[0][1]) / actual_flags[0][1]

    for i in range(len(actual_flags)):
        flag_comparison.append(actual_flags[i] == pred_flags[i])

    algo_accuracy = np.sum(flag_comparison[1:]) / 8

    result = [HR_error, SBP_error, algo_accuracy] + actual_flags[1:] + pred_flags[1:]

    return result


def accuracy_f1(true_positive, true_negative, false_positive, false_negative):
    """
    Calculates accuracy and F1-score for a particular feature.

    true_positive : number of true positives.
    true_negative : number of true negatives.
    false_positive: number of false positives.
    false_negative: number of false negatives.

    output:    acc: accuracy of the model on the feature.
          f1_score: F1-score of the model on the feature.
    """
    acc = (true_positive + true_negative) / (true_positive + false_positive + false_negative + true_negative)
    prec = true_positive / (true_positive + false_positive)
    rec = true_positive / (true_positive + false_negative)
    f1_score = 2 * (rec * prec) / (rec + prec)

    return acc, f1_score
