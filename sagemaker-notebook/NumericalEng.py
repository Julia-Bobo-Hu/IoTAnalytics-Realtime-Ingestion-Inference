# ----------------------------------------------------------------------------
# File name: NumericalEng.py
#
# Created on: Aug. 11 2020
#
#  by Julia Hu
#
# Description:
#
# 1) This module to engineer numerical features
#
#       
#
# -----------------------------------------------------------------------------
#first load in all necessary librares 
import pandas as pd
import numpy as np
import datetime
from sklearn.base import BaseEstimator, TransformerMixin
#Custom transformer we wrote to engineer features ( bathrooms per bedroom and/or how old the house is in 2019  ) 
#passed as boolen arguements to its constructor
class NumericalTransformer(BaseEstimator, TransformerMixin):
    #Class Constructor
    def __init__( self, floor_cal=True, square_log=True,time_process=True, years_old=True):

        self._floor_cal = floor_cal
        self._square_log = square_log
        self._time_process = time_process
        self._years_old = years_old
        
    #Return self, nothing else to do here
    def fit( self, X, y = None ):
        return self 
    
    #Custom transform method we wrote that creates aformentioned features and drops redundant ones 
    def transform(self, X, y = None):
        #Check if needed 
 
        if self._floor_cal:
            X.loc[:,'floor_area'] = X.square_feet / X.floor_count
            
        if self._square_log: 
            X.loc[:,'square_feet'] =  np.log1p(X['square_feet'])
        
        if self._time_process:
            # Add more features
            X.loc[:,"week"] = X["timestamp"].dt.week
            X.loc[:,"month"] = X["timestamp"].dt.month    
            
        #Check if needed     
        if self._years_old:
            #create new column
            X.loc[:,'yr_built'] =  2020 - X['year_built']

         
        # Sort by timestamp
        X.sort_values("timestamp", inplace=True)
        X.reset_index(drop=True, inplace=True)
        X = X.drop(["floor_count",'year_built'], axis = 1 )
    
        #returns a numpy array
        return X