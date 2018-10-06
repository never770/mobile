# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:14:29 2018

@author: never770
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv("D://study//game//mobile//test_datas.csv") # https://www.cnblogs.com/guochangyu/p/7788414.html


#data = pd.read_csv("https://github.com/zefang/Mobile-carrier-competition/raw/master/datas.csv") # read online data https://blog.csdn.net/Maverick_7/article/details/79026887
#print(data.head())

#x,y = data.drop(['user_id','current_service','service_type'], axis=1).as_matrix(),data.loc[:,'service_type'].as_matrix() # https://blog.csdn.net/sinat_29957455/article/details/79477940
#x,y = data.drop(['user_id','current_service'], axis=1).as_matrix(),data.loc[:,'current_service'].as_matrix() # https://blog.csdn.net/sinat_29957455/article/details/79477940
##np.unique(A)
#print(len(np.unique(y)))
#train_data, test_data, train_labels, test_labels = train_test_split(x,y,test_size=0.2,random_state=0)
##train_x = data.drop(['user_id','current_service'], axis = 1)
##train_y = data.loc[:, 'current_service'] 
#selected_features = data.columns.values.tolist()
#selected_features.remove('user_id')
#selected_features.remove('user_id')
