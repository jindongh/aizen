# aizen
1. download users.sql from https://app.asana.com/0/164562914962707/164698328539659
2. convert data from sql to csv: ./sql2csv
3. normalize data: python normalize.py
4. test:
4.1 input: 60k training set, a user, an app
4.2 output: predict whether the user will install the app.
