#Pregunta 5:
# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente 
# todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

#Funcion que genera una lista de un rango  
def listas(rango):
    #Genera la lista a partir del parametro "rango"
    ls = [i for i in range(1,rango+1)]
    #retorna el rango generado en una lista "ls"
    return ls

#Funcion suma, suma la lista generada y las suma
def suma(rango):
    #Lista generada a partir de la funcion "listas" donde lleva por paramerto rango para realizar la suma 
    ran = listas(rango)
    #suma toda la lista
    sumas = sum(ran)
    #muestra la suma
    return sumas

#Funcion de multiplicacion
def multiplicacion(rango):
    #acumula y multiplica los numeros de la lista
    n=1
    #Lista generada a partir de la funcion "listas" donde lleva por paramerto rango para realizar la suma 
    ran = listas(rango)
    #Bucle recorre la variable ran que contiene la lista generada a partir del parametro "rango"
    for i in list(ran):
        #Acumulador multiplicara el bucle para obtener el resultado final
        n=n*i
        t=n
    #retorna la lista t
    return t
#ingresar un numero que es el rango la cual sera la lista presentada
numero = int(input('Calcular la suma de numeros consecutivos de 1 hasta: '))
#Mostrara la lista
print(f'lista: {listas(numero)}')
#suma la lista
print(f'Suma: {suma(numero)}')
#multiplica la lista
print(f'Producto: {multiplicacion(numero)}')
