#!/bin/env python
# -*- coding: UTF-8 -*-
import normalize
import pandas
from sklearn.linear_model import LogisticRegression

# 80% of the dataset will be used to do training.
SRC_CSV='final.users.csv'
SRC_CSV='users.csv'
TRAIN_RATIO = 0.8
print 'Loading data from csv'
info=pandas.read_csv(SRC_CSV, error_bad_lines=False, warn_bad_lines=True)
print 'Normalize data'
info, dicts = normalize.normalize(info)

print 'Create training set'
train_size = info.shape[0] * TRAIN_RATIO
if info.shape[0] - train_size > 100:
	train_size = info.shape[0] - 100 
print 'Total: %d train_size:%d' % (info.shape[0], train_size)
train_set = info.loc[:train_size]
test_set = info.loc[train_size+1:]

target_selector = dicts.appids[0]
target_app='谷歌拼音输入法'
target_selector = dicts.appnames[target_app]
dicts.appids.remove(target_selector)
train_selectors = dicts.otherids + dicts.appids
train_target = train_set[target_selector]
test_target = test_set[target_selector]

model = LogisticRegression()
print 'Begin training'
model.fit(train_set[train_selectors], train_target)
print 'Begin predict'
test_result = model.predict(test_set[train_selectors])

for a,b,c in zip(test_set.iterrows(), test_target, test_result):
	print a[0],b,c
