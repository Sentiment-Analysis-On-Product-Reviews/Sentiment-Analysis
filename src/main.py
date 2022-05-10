# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:17:58 2022

@author: AneeshDixit
"""

import pandas as pd
from StoringReviews import StoringReviews
from LanguageProcessor import *

review_obj = StoringReviews()

reviews_df, reviews_list = review_obj.storeReviews()
