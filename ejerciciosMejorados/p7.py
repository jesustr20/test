#Pregunta 7:
#Desarrollar una funcion que me devuelva el n-esimo fibonacci
#Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
#el fibonacci(3) = fibonacci(2) + fibonacci(1)
#
#Nota: Implementarlo de modo iterativo.

def fibonacci(index):
    fib=[]
    a,b=1,0
    for i in range(index):
        a,b=b,a+b
        fib.append(a)
        #total = a,b=b,a+b
        print(f'{i}: \t',a,'+',b,'=\t',a+b)
    return fib
    
index = int(input('Escribe el Nsimo fibonacci: '))
print('Indice - fibonacci - Resultado')
print(fibonacci(index))