arq = open('novo.txt','w')

arq.write('Estudando \n')

arq.close()

arq = open('novo.txt', 'a+' )

arq.write('Machine \n')

print(arq.encoding)


arq.close()


arq = open('novo.txt', 'a+' )



arq.write('Learning!! \n')

arq.flush()
arq.seek(0)
print(arq.read())

arq.close()
with open('novo.txt', 'a' ) as fileFunc:
    fileFunc.write("blabalbablabalba ")

