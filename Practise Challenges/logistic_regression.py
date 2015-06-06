__author__ = 'Sagar'

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math

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
df['Intercept'] = 1.0
ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']

# print df
print ind_vars

logit = sm.Logit(df['IR_TF'], df[ind_vars])
logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()

coeff = result.params
print coeff


def logistic_function(fico_score, loan_amount, coeff):
    prob = 1 / (1 + math.exp(coeff[0] + coeff[2] * fico_score - coeff[1] * loan_amount))
    if prob < 0.7:
        p = 1
    else:
        p = 0
    return prob, p

prob = logistic_function(720, 1000, coeff)[0]
p = logistic_function(720, 1000, coeff)[1]