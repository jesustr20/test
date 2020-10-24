#Pregunta 2:
# Escribir un codigo en python que sume y multiplique respectivamente 
# todos los numeros de una lista, ejemplo;
# Numeros=1 2 3 4, suma 10, multiplicacion 24.

def sumaProducto(rango):
    mi_lista = []
    suma = 0
    producto = 1
    for i in range(1,rango+1):
        mi_lista.append(i)
    for j in list(mi_lista):
        suma = suma + j
        producto = producto * j
        tsuma = suma
        tprod = producto
        print(j)
    print(f'Suma Total: {tsuma}')
    print(f'Producto Total: {tprod}')

ran = int(input('Ingresa un rango de numeros: '))
print(sumaProducto(ran))