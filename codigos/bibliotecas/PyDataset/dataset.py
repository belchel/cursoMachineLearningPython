import pandas as pd
import pydataset as pset
from datetime import datetime


# print(pset.data())  #quais datasets essa lib possui


titanic =  pset.data('titanic')
##
##print(titanic.head(10))  # retorna os 10 primeiros elementos
##
##
##print(titanic.tail(10)) # retorna os 10 ultimos elementos
##
##
##print(titanic.describe())
##
##
##print(titanic['class'].value_counts())  # como se fosse um count com group by 


print('bytes antes = '+ str(titanic['class'].nbytes)) #quanto de memoria esta sendo utilizado




# code to speed test


tstart = datetime.now()
titanic['class']== '3rd class'
tend = datetime.now()
tend = tend - tstart
print('tempo gasto antes = '+ str(tend.microseconds))


titanic['class']== titanic['class'].astype('category')



print('bytes depois = '+ str(titanic['class'].nbytes))

tstart = datetime.now()
titanic['class']== '3rd class'
tend = datetime.now()
tend = tend - tstart
print('tempo gasto depois = '+ str(tend.microseconds))




