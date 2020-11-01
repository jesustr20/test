# Pregunta 1: 
# Generar un codigo en python que sume 10 numeros aleatorios de la siguiente 
# forma: los 5 mas bajos y los 5 mas altos
from random import randint


#Primera forma:
#Lista = lista aleatoria de numeros desordenados
print("##### PRIMERA FORMA#####")
print("############################")
lista = [1,6,14,8,3,10,11,23,45,12]
#Recorrera la lista llamada "lista"
for i in list(lista):
    #Ordenada la lista de forma ascendente
    orden = sorted(lista)
    #Cogera los 5 primeros numeros de forma ascendente por ello "[:5]" donde indica que solo muestre los 5 primeros numeros
    cinco_menor = orden[:5]
    #cogera los 5 ultimos digitos de una lista [5:]
    cinco_mayor = orden[5:]
    #sumara los 5 digitos de los 5 primeros numeros
    tme = sum(cinco_menor)
    #sumara los 5 digitos de los 5 ultimos numeros
    tma = sum(cinco_mayor)
#Muestra la lista natural al ejecutarse el programa
print('Lista natural: ',lista)
#Muestra la lista en orden ascendente
print('Lista Ordenada: ',orden)
#Muestra la suma de los 5 primeros numeros
print('5 num menores: ',cinco_menor,': Suma: ',tme)
#Muestra la suma de los 5 ultimos numeros
print('5 num mayores: ',cinco_mayor,': Suma: ',tma)

#################################################
print("\n")
print("##### SEGUNDA FORMA FORMA (MISMO RESULTADO) #####")
print("############################")
#Segunda forma:
#Lista2 = Es una lista aleatoria
lista2= lista = [1,6,14,8,3,10,11,23,45,12]
#Ordenada la lista de forma ascendente
orden=sorted(lista2)
#Muestra la lista natural al ejecutarse el programa
print('Lista natural: ',lista2)
#Muestra la lista en orden ascendente
print('Lista Ordenada: ',orden)
#Muestra la suma de los 5 primeros numeros, "orden[:5] mostrara los 5 primeros numeros ordenados"
#Sum(orden[:5]) : suma los 5 primeros numeros
print('5 num menores: ',orden[:5],': Suma: ',sum(orden[:5]))
#Muestra la suma de los 5 ultimos numeros, "orden[:5] mostrara los 5 ultimos numeros ordenados"
#Sum(orden[5:]) : suma los 5 ultimos numeros
print('5 num mayores: ',orden[5:],': Suma: ',sum(orden[5:]))

#############################################################

#Tercera Forma
#Funcion la cual al ingresar un numero mostrara una lista de numeros desordenados de un rango especifigo de numeros
def sumaMenorMayor(numero):
    #mostrara un rango de numeros desordenados en una lista y range mostrara la canidad de numeros que es 10
    #si el rango de numeros aleatorios seria 1, 5 la lista de 10 numeros seria [1,3,4,2,5,5,2,3,1,1]
    number_list = [randint(1,numero) for x in range(10)]
    #Sorted mostrara la lista desordenada de manera ordenada en ascendente
    orden = sorted(number_list)
    #Mostrara la lista desordenada
    print(f'Lista Desordenada: {number_list}')

    return orden 

print("\n")
print("##### TERCERA FORMA FORMA (DISTINTO RESULTADO) #####")
print("############################")
#Ingresar un numero como ultimo rango p
cantidad = int(input('Rango de Numero aleatorio: '))
#LLama a la funcion "sumaMenorMayor" a la cual le pasara el parametro "cantidad"
ordenada= sumaMenorMayor(cantidad)
#Mostrara la lista de numeros aleatorios de manera Desordenada y Ordenada
print(f'Lista Ordenada: {ordenada}')
#Mostrara los 5 primeros numeros de la lista ordenada y los sumara
print(f'5 menores: {ordenada[:5]}, Suma: {sum(ordenada[:5])}')
#Mostrara los 5 ultimos numeros de la lista ordenada y los sumara
print(f'5 mayores: {ordenada[5:]}, Suma: {sum(ordenada[5:])}')
