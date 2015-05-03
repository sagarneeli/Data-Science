__author__ = 'Sagar'

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)
frequency = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(frequency.keys(), frequency.values(), width=1)
# plt.show()

chi, p = stats.chisquare(frequency.values())


print "Chi-squared test :" + str(chi) + "," + str(p)
