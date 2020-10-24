#Pregunta 6: 
# Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es decir, 
# abierto '(' y cerrado ')'. 
# Ejm: 
#  Entrada: '(()()())()()(())'
#  Salida: True
#  Entrada: '(()('
#  Salida: False

l = []
par = True
nombre = input('ingresa parentisis: ')
for i in nombre:
    l.append(i)
    if l == ')' or i=='(':
        par = False
    elif l == '()':
        par= True
    print(par)
print(l)

    