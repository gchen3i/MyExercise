# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

data_dir ='/Users/gangch/python/data'

orig_data  = pd.read_csv('%s/龙虎榜.csv' %data_dir,skiprows=1,sep=',',encoding='utf_8_sig')
