#Pregunta 1:
#  Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: 
# los 5 mas bajos y los 5 mas altos

from random import randint

def numAle():
    c = []
    suma = 0
    for i in range(1,11):
        r = randint(1,50)
        suma= suma +r
        c.append(r)
    #sor = sorted(c)
    sorDer = sorted(c, reverse=False)[0:5]
    sorIzq = sorted(c, reverse=False)[5:]
    print(f'Lista Aleatoria: {c}')
    #print(f'Lista Ordenada: {sor}')
    print(f'Los 5 mas bajos: {sorDer}')
    print(f'Los 5 mas altos: {sorIzq}')
    print(f'Suma 10 numeros aleatorios: {suma}')

print(numAle())

#Version2 del codigo
#Suma de Numeros aleatorios por cantidad:

def numAletorio(ran1, ran2):
    c = []
    suma = 0
    for i in range(1,11):
        r = randint(ran1,ran2)
        suma= suma +r
        c.append(r)
    #sor = sorted(c)
    sorDer = sorted(c, reverse=False)[0:5]
    sorIzq = sorted(c, reverse=False)[5:]
    print(f'Lista Aleatoria: {c}')
    #print(f'Lista Ordenada: {sor}')
    print(f'Los 5 mas bajos: {sorDer}')
    print(f'Los 5 mas altos: {sorIzq}')
    print(f'Suma 10 numeros aleatorios: {suma}')


ran1 = int(input('Elige el perimer punto del rango: '))
ran2 = int(input('Elige el segundo punto del rango: '))

print(numAletorio(ran1, ran2))
