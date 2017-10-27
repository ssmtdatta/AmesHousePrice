### Ames House Prices: EDA and Price Prediction

A day's work - wanted to see what we could do in a day (6 to 8 hours)  

**About the data:**
The [Ames Housing dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques#description) is available to through Kaggle.

**Base Directory:** `AmesHousing/`

**Sub-directories:**  

`DataDwn/`  
Download and place raw data here.



`EDA/`  
Notebooks showing exploratory analysis.
- **data_peek.ipynb**  
Take a first look at the data.
- **data_features_summary_stat.ipynb**  
Obtain a statistical summary of the data.
- **data_features_distribution.ipynb**  
Explore and visualize the distribution and trend of the features.
- **data_features_univariate_corr.ipynb**
Explore the linear correlation between the features and the target.

`SupportModule/`  
Helper functions and parameter files.
* **lookup_dir_names.py**  
Directory path names are stored here as parameters. User can define and access dir names from this file.
* **lookup_feature_names.py**  
Raw data features names and feature names separated by category are stored. User can combine different features in codes from here.
* **fnc_featureSelection.py**  
A user defined module. Contains functions to combine and engineer raw features in certain ways.

`Prediction/`  
Linear regression and random forest so far.   
