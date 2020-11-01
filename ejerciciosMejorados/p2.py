#Pregunta 2: 
# Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista, ejemplo; 
# Numeros=1 2 3 4, suma 10, multiplicacion 24.

#Contador sumara los numeros de un rango
suma=0
#Contador multiplicara los numeros de un rango
prod=1
#El bucle For recorrara el rango indicado en su parametro "range"
for i in range(1,15+1):
    #Sumara los numeros dentro del rango
    suma = suma+i
    #Multiplica los numeros dentro del rango indicado
    prod=prod*i
    #imprime el rango de numeros
    print(i)
#Muestra la suma total del rango de numeros
print(f'Suma: {suma}')
#Muestra el producto total del rango de numeros
print(f'Prod: {prod}')