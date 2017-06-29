import pandas as pd

copa = pd.read_csv('copacabana.csv', delimiter = ';')

#print(copa)

#print(copa['Quartos'].describe())


#print(copa.loc[copa['Quartos'] == 5])

copa['TOTAL'] = copa['AreaConstruida'] * copa['VAL_UNIT']

print(copa['TOTAL'].describe())




