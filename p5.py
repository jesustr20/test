#Pregunta 5: 
# Escribir una funcion sum() y una función multip() que sumen y multipliquen 
# respectivamente todos los números de una lista. 
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


def listaNum(ran):
    r = []
    for i in range(1,ran+1):
        r.append(i)
    return r

def sumar(ran):
    listas = listaNum(ran)
    n = 0
    for i in list(listas):
        n = n+ i
        tsuma=n
    return tsuma

def producto(ran):
    listas = listaNum(ran)
    n=1
    for i in list(listas):
        n=n*i
        tprod=n
    return tprod
        
rango = int(input('Escribe un rango de numeros: '))
print(f'Lista: {listaNum(rango)}')
print(f'Suma: {sumar(rango)}')
print(f'Producto: {producto(rango)}')