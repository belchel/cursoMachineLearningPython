
age = int(input('Digite a idade: '))


if age>18 :
    print('maior de idade')
elif age == 18:
    print('EXATAMENTE 18')
else:
    print('menor de idade')



while age>0:
    print('reduzindo %d' % age)
    age-=1


for letter in 'Python':
   print ('Current Letter :', letter)

for i in range(1, 10, 2):
    print(i, end='+')