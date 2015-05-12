__author__ = 'Sagar'

import pandas as pd
import csv

# with open('loansData_clean.csv','rU') as inputFile:
#     inputReader = csv.reader(inputFile)
#     for line in inputReader:
#         print line

df = pd.read_csv('loansData_clean.csv')


for index in range(len(df['Interest.Rate'])):
    if df['Interest.Rate'].values[index] < 0.12:
        df.loc[index, 'IR_TF'] = 0
    elif df['Interest.Rate'].values[index] >= 0.12:
        df.loc[index, 'IR_TF'] = 1


print df['IR_TF']
print df[df['Interest.Rate'] == 10].head() # should all be True
df[df['Interest.Rate'] == 13].head() # should all be False


ind_vars = list(df)

print ind_vars