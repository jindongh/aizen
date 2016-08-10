#!/bin/env python
import normalize
from sklearn.linear_model import LogisticRegression

# 80% of the dataset will be used to do training.
SRC_CSV='final.users.csv'
SRC_CSV='users.csv'
TRAIN_RATIO = 0.9
info=pandas.read_csv('users.csv', error_bad_lines=False, warn_bad_lines=True)
info, dicts = normalize.normalize(info)

train_size = info.shape[0] * TRAIN_RATIO
# test 100
train_size = info.shape[0] - 100
train_set = info.loc[:train_size]
test_set = info.loc[train_size+1:]

selectors = dicts.otherids + dicts.appids[1:]
train_target = train_set[dicts.appids[0]]
test_target = test_set[dicts.appids[0]]

model = LogisticRegression()
model.fit(train_set[selectors], train_set[target])
test_result = model.predict(test_set[selectors])

for i in range(len(test_result)):
	print test_set.loc[i]['id'],test_result.loc[i], test_target.loc[i]
