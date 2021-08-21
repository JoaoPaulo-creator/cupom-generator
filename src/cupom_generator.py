from random import randint as ri



letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = ''
numeros = '0123456789'
n = ''


for i in range(0,3):
    #Randomizando letras
    randomizar_letras = ri(0, len(letras))
    l += letras[randomizar_letras: randomizar_letras +1]


for p in range(0,2):
#Randomizando números
    randomizar_numeros = ri(0, len(numeros))    
    n += numeros[randomizar_numeros: randomizar_numeros + 1]


print(f'{l}{n}')
