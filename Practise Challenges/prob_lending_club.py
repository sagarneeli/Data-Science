__author__ = 'Sagar'

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Funded.By.Investors')

plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

loansData.boxplot(column='Amount.Requested')
plt.show()

frequency = collections.Counter(loansData['Open.CREDIT.lines'])



