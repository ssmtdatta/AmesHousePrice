"""
Select and combine/define/refine features from the raw data.
The moldule "LookUp.lookup_feature_names.py" contain the feature names. Feature names are read
from this file and combine according to "combineFeatures_*" function.
""" 


# #Python modules
import pandas as pd
import numpy as np
from datetime import datetime as dt

# #Support modules
import lookup_feature_names as FEATURE


global yr
yr = dt.today().year


def combineFeatures_01(_df_):
	"""
	INPUT: _df_  the raw dataframe
	OUTPUT: separate dataframes with numerical, categorical and dummy variables.
	"""
	feature_names = FEATURE.feature_lot \
					+ FEATURE.feature_floor \
					+ FEATURE.feature_basement \
					+ FEATURE.feature_bathroom \
					+ FEATURE.feature_garage \
					+ FEATURE.feature_porch \
					+ FEATURE.feature_pool \
					+ FEATURE.feature_fireplace \
					+ FEATURE.feature_year \
					+ FEATURE.feature_hood \
					+ FEATURE.feature_building \
					+ FEATURE.feature_quality

	df = _df_[feature_names]
	df = df.fillna(0)
	

	# #numeric
	num_df = pd.DataFrame()
	num_df['TotLotSF'] = df['LotArea'] + df['LotFrontage']
	num_df['TotFlrSF'] = df['1stFlrSF']+ df['2ndFlrSF'] + df['GrLivArea'] + df['LowQualFinSF']
	num_df['TotalBsmtSF'] = df['TotalBsmtSF']
	num_df['TotNumBath'] = df['BsmtFullBath']+df['BsmtHalfBath']+df['FullBath']+df['HalfBath']
	num_df['GarageArea'] = df['GarageArea']
	num_df['PorchArea'] = df['WoodDeckSF']+df['OpenPorchSF']+df['EnclosedPorch']+df['3SsnPorch']+df['ScreenPorch']
	num_df['PoolArea'] = df['PoolArea']
	


    # #categorical
	ctg_df = pd.DataFrame()
	ctg_df['Year'] = 1/(yr-df['YearRemodAdd']) # numeric but ... not a measurement

	ctg_df['isGarage'] = df['GarageCars']  # Garage
	tmp = np.array(ctg_df['isGarage'].tolist())
	ctg_df['isGarage'] = np.where(tmp > 0, 1, tmp).tolist()

	ctg_df['isFireplace'] = df['Fireplaces']
	tmp = np.array(ctg_df['isFireplace'].tolist())
	ctg_df['isFireplace'] = np.where(tmp > 0, 1, tmp).tolist()

	ctg_df['isPorch'] = num_df['PorchArea']
	tmp = np.array(ctg_df['isPorch'].tolist())
	ctg_df['isPorch'] = np.where(tmp > 0, 1, tmp).tolist()

	ctg_df['isPool'] = num_df['PoolArea']
	tmp = np.array(ctg_df['isPool'].tolist())
	ctg_df['isPool'] = np.where(tmp > 0, 1, tmp).tolist()


	# dummy features
	dummy_df = pd.DataFrame()
	dummy_df['GarageCars'] = df['GarageCars'].astype(str)
	dummy_df['OverallQual'] = df['OverallQual'].astype(str)
	dummy_df['OverallCond'] = df['OverallCond'].astype(str)
	dummy_df['Neighborhood'] = df['Neighborhood']
	dummy_df['BldgType'] = df['BldgType']
	dummy_df = pd.get_dummies(dummy_df)

	return num_df, ctg_df, dummy_df

  

def combineFeatures_02(_df_):
	"""
	INPUT: _df_  the raw dataframe
	OUTPUT: data frame with selected numerical features
	"""
	feature_names = FEATURE.feature_lot \
					+ FEATURE.feature_floor \
					+ FEATURE.feature_basement \
					+ FEATURE.feature_bathroom \
					+ FEATURE.feature_garage \
					+ FEATURE.feature_porch \
					+ FEATURE.feature_pool \
					+ FEATURE.feature_fireplace \
					+ FEATURE.feature_year 

	df = _df_[feature_names]
	df = df.fillna(0)

	return df





