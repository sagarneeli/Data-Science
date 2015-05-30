__author__ = 'Sagar'

import pandas as pd
import csv
import statsmodels.api as sm

# with open('loansData_clean.csv','rU') as inputFile:
#     inputReader = csv.reader(inputFile)
#     for line in inputReader:
#         print line

df = pd.read_csv('loansData_clean.csv')

# print df.head()
# print df.columns

for index in range(len(df['Interest.Rate'])):
    if df['Interest.Rate'].values[index] < 0.12:
        df.loc[index, 'IR_TF'] = 0
    elif df['Interest.Rate'].values[index] >= 0.12:
        df.loc[index, 'IR_TF'] = 1


# print df['IR_TF']
# print "Here"
# print df[df['Interest.Rate'] == 10].head() # should all be True
# df[df['Interest.Rate'] == 13].head() # should all be False

# print df.head()
df['intercept'] = 1.0
ind_vars = list(df)

# print df
# print ind_vars

logit = sm.Logit(df['IR_TF'], df[ind_vars])
logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()

coeff = result.params
print coeff