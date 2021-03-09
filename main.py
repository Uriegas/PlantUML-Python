import os

class Funcion:
    def __init__(self):
        self.nombre
        self.parametros = []
        self.retorno

class Dato:
    def __init__(self):
        self.nombre
        self.tipodedato

class Clase:
    def __init__(self):
        self.datos = []
        self.funciones = []

    def addDato(self, dato):
        self.datos.append(dato)
        
    def addFuncion(self, func):
        self.funciones.append(func)

class GeneradorPlantUMLTxt:
    def __init__(self):
        self.t
        self.nombreArchivo = '';
        self.clases = []
        self.relaciones = []

    def leerArchivoaClase(self, nombre):
        self.archivo = open(nombre)
        clase = Clase()
        ##Codigo
        return clase
    
    def claseaString(self, clase):
        self.claseString = ''
        ##Codigo
        return self.claseString
    
    def imports(self):
        self.importStrings = ''
        #Codigo
        return self.importStrings
        

#Primero obtener los archivos
#Despues buscar las clases
#Las funciones de las clases
#Las relaciones de las clases
#Información en: https://plantuml.com/class-diagram

#El programa genera un txt
#Ese txt se manda a plantuml
#Finalmente se muestra el diagrama


#Esta parte crea el .png y lo abre
os.system("java -jar plantuml.jar salida.txt") # Termine sin error
os.system("xviewer Clases.png") # Archivo existe
