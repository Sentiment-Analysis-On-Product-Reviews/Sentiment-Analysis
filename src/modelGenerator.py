# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:38:01 2022

@author: AneeshDixit
"""

import pandas as pd
import csv

tsv_file = open('../Data/wikiDetoxAnnotated40kRows.tsv')

read_tsv = csv.reader(tsv_file, delimiter='\t')

for row in read_tsv:
    print(row)
