import pandas as pd
import numpy as np


df = pd.read_csv('primary-results.csv')


#print(df.groupby('candidate').aggregate({'votes': [min, np.mean, max]}))


#print(df[df['votes']==590502])


#print(df.groupby('candidate').aggregate({'fraction_votes': [min, np.mean, max]}))

      


#print(df[(df['fraction_votes']==1) & (df['candidate']=='Hillary Clinton')])




def fraction_votes_filter(x):
    return x['votes'].sum()>1000000


print(df.groupby('state').filter(fraction_votes_filter))


print(df.groupby(['state_abbreviation','candidate'])['votes'].sum())
