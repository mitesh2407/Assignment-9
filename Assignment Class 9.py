# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:25:26 2019

@author: acer
"""

#####################       Assignment 9        #######################################
#   Read the dataset from the below link
#   https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US
#          _Baby_Names/US_Baby_Names_right.csv

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import math as m
import seaborn as sns
import time

# filepath =
'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/'

# df = pd.read_csv(filepath + 'US_Baby_Names_right.csv',dtype={'Frequency': float})

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head(5)