#Pregunta 6:
#Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es decir,
#abierto '(' y cerrado ')'.
#Ejm:
# Entrada: '(()()())()()(())'
# Salida: True
#
# Entrada: '(()('
# Salida: False



cadena = input('Ingresa ( o ): ')

l = [i for i in cadena]
a = l.count('(')
b = l.count(')')

if a==b:
    print(True)
if a!=b:
    print(False)
print(f'Cantidad "(": {a}, \nCantidad ")": {b}')