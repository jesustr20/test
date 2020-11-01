import os, time, datetime


#lista = 'E:/lista'
def prueba():
    try:
        lista = 'E:/lista'
        for namePath in os.listdir(lista):
            print(namePath)
    except FileNotFoundError as e:
        return f'No existe el archivo: {e}'
    except NotADirectoryError as e:
        return f'Error: {e}'


#directory = ''
#contenido = os.listdir(directory)
#
#imagenes = []
#for fichero in contenido:
#    if os.path.isfile(os.path.join(directory, fichero)) and fichero.endswith('.jpg'):
#        imagenes.append(fichero)
#print(imagenes)

directory = input('Ingresa un directorio: ')

with os.scandir(directory) as ficheros:
    print('######################')
    print(f'Carpeta Principal: {directory}')
    for fichero in ficheros:
        nombre = fichero.name
        tamaño = os.stat(fichero).st_size
        tiempo = os.path.getmtime(fichero)
        tf = datetime.datetime.fromtimestamp(tiempo)
        fcreacion = time.ctime(os.path.getctime(fichero))
        #ultima modif
        modifv2 = os.stat(fichero)
        umodifv2=time.localtime(modifv2.st_mtime)
        umodifv2= datetime.datetime(umodifv2[0],umodifv2[1],umodifv2[2],umodifv2[3],umodifv2[4],umodifv2[5],)
        print(f'Nombre: {nombre}')
        print(f'Tamaño: {tamaño}')
        print(f'fecha creacion: {fcreacion}')
        print(f'Ultima modif: {umodifv2}')
        print('######################')