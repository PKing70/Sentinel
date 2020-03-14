# SARIMA
Sentinel Healthcare SARIMA Notebook

This SARIMA model is built using the SARIMAX model in the statmodel.statespace package. 

Datasets: 
| dataset name  | purpose  |
| :------------ |:------------| 
| vitals2.csv     | the raw dataset | 
| combined_vitals.csv     | the new raw dataset | 
| vitals_sbp_interpolated.csv     | aggregated per day and gaps interpolated, for SBP |
| vitals_hr_interpolated.csv     | aggregated per day and gaps interpolated, for HR |
| vitals_combined_interpolated.csv      | combined dataset with aggregations and interpolations SBP and HR |
| df_vitals_combined_SBP_predicted.csv     | the predictions generated using SARIMAX model for SBP |
| df_vitals_combined_SBP_forecast.csv     | the future forecast generated using SARIMAX model for SBP |
| df_vitals_combined_HR_predicted.csv     | the predictions generated using SARIMAX model for HR |
| df_vitals_combined_HR_forecast.csv     | the future forecast generated using SARIMAX model for HR |
| sarima_models_stats.csv     | model stats for SARIMAX model |
| sarima_flags_stats.csv     | flags stats for SARIMAX model |


From Jupyter Notebooks in your browser, navigate to your local/clone of this repo and run each of the notebooks mentioned below.

##for explorations: 
| notebook name  | input  | output |
| :------------ |:------------| :------------|
| vitals_etl_explore_different_cosinor_models     | vitals2.csv | None |
| vitals_etl_explore_cosinor_interpolation_with_charts      | vitals2.csv        |   None |
| sarima_exploratory_work_with_charts | vitals_combined_interpolated.csv        |    None |

##for data preprocessing (day level aggregations and cosinor interpolation): 
| notebook name  | input  | output |
| :------------ |:------------| :------------|
| vitals_etl_cosinor_interpolation_newdata_SBP_multicore     | combined_vitals.csv | vitals_sbp_interpolated.csv |
| vitals_etl_cosinor_interpolation_newdata_HR_multicore      | combined_vitals.csv        |   vitals_hr_interpolated.csv |
| vitals_combine_the_two_interpolated_datasets | vitals_sbp_interpolated.csv & vitals_hr_interpolated.csv        |    vitals_combined_interpolated.csv |

##for modelling and predictions:
| notebook name  | input  | output |
| :------------ |:------------| :------------|
| sarima_prediction_and_forecast_sbp     | vitals_combined_interpolated.csv | df_vitals_combined_SBP_predicted.csv & df_vitals_combined_SBP_forecast.csv |
| sarima_prediction_and_forecast_hr | vitals_combined_interpolated.csv        |    df_vitals_combined_hr_predicted.csv & df_vitals_combined_hr_forecast.csv |


##for generating the metrics:
| notebook name  | input  | output |
| :------------ |:------------| :------------|
| generate_sarima_metrics     | vitals_combined_interpolated.csv, df_vitals_combined_SBP_predicted.csv & df_vitals_combined_hr_predicted.csv | sarima_models_stats.csv |
| generate_sarima_flags | vitals_combined_interpolated.csv, df_vitals_combined_SBP_predicted.csv & df_vitals_combined_hr_predicted.csv        |    sarima_flags_stats.csv |