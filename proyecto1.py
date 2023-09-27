import os

CARPETA = 'contactos/' # carpeta de contactos
EXTENSION = '.txt' # extension de archivos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria 

def app():
    # revisa si la carpeta existe
    crear_directorio()

    # muestra el menu de opciones
    mostrar_menu()

    #preguntar accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        # ejecutar opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
           mostrar_contactos()
           preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')


def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado')
    except:
        print('No existe el contacto')

        app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que sea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

            app()
    except IOError:
        print('El archivo no existe')
        print(IOError)
        app()

def editar_contacto():
    print('Escribe el nombre contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    # revisar si el contacto ya existe antes de editar
    existe = existe_contacto(nombre_anterior) 

    if existe:
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # resto de los campos
            nombre_contacto = input('Nuevo Nombre del contacto: \r\n')
            telefono_contacto = input('Agrega el Nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega Nuevo categoria: \r\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #renombrar archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar mensaje de exito
            print('Contacto modificado con exito')

    else:
        print('Ese contacto no existe')

    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    # Recorrer el iterador para asegurar que los archivos son txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]


    for archivo in archivos_txt: 
        with open (CARPETA + archivo) as contacto:
    
            for linea in contacto:
                # imprime los contactos
                print (linea.rstrip())
            # separador
            print('\r\n')
       
def agregar_contacto():
    print('escribe los datos para agregar contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')

    # revisar si el contacto ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto) 

    if not existe:

        with open (CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # resto de los campos
            telefono_contacto = input('Agrega el Telefono: \r\n')
            categoria_contacto = input('Agrega categoria: \r\n')

            # instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribir dentro del archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Mostrar un mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Este contacto ya existe')
        
        app()

def mostrar_menu():
    print('Seleccione una opcion del menu: ')
    print('1. Agregar Nuevo Contacto')
    print('2. Editar contacto')
    print('3. Ver Contactos')
    print('4. Buscar Contacto')
    print('5. Eliminar contacto')

def crear_directorio():
     if not os.path.exists(CARPETA):
    #crear carpeta
         os.makedirs(CARPETA)
            

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)  


app()