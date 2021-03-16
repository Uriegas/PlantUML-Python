import os

class Clase:
    def __init__(self):
        self.nombre = ""
        self.datos = []
        self.funciones = []

    def __str__(self):
        #Convertir esta clase a string, segun el formato de Plantuml
        #Kuroro
        s = "class " + self.nombre + '\n'
        for var in self.datos:
            s += var + '\n'
        for fun in self.funciones:
            s += "+ " + fun + '\n'
        return s


class GeneradorPlantUMLTxt:
    def __init__(self):
        self.nombreArchivo = ""
        self.clases = []
        self.relaciones = ""

    def leerArchivoaClase(self, nombre):
        self.archivo = open(nombre)
        Lines = self.archivo.readlines()
        clase = Clase()
        ##Codigo
        for line in Lines:
            if(len(line) != 0):
                #Eliminar tabs y salto de linea
                line = line.replace('\n', '')
                line = line.replace('\t', '')

                #Analisis de la linea
                words = line.split(' ')
                if(words[0] == "class"):
                    if(clase.nombre):
                        self.clases.append(clase)
                        clase = Clase()
                    #Split name of class to remove: ()
                    words[1] = words[1].replace(':', '')
                    names = words[1].split('(')
                    clase.nombre = names[0]
                elif(words[0] == "def"):
                    line = line.replace("def ", '')
                    line = line.replace(':', '')
                    clase.funciones.append(line)
#                elif(words[0] == "return"):
#                    line = line.replace("return ", '')
#                    fun = clase.funciones.pop()
#                    line = line + ' ' + fun
#                    clase.funciones.append(line)
                elif(words[0].find("self.") != -1):
                    variables = words[0].split('.')
                    clase.datos.append(variables[1])
        self.clases.append(clase)
        return clase
        
    def imports(self):
        importStrings = ''
        temp = ''
        name = []
        abecedario = ["a", "b", "c", "d", "e"] #Ni me preguntes alab, ando rabiosa
        auxlen = 0
        auxcad = ''
        # Lo guarda en un arreglo sin los parentesís
        with open('Final.py', 'r') as f:
            for linea in f:
              temp =(linea[0:linea.find('c') + 5])  
              if (temp == 'class'):
                auxcad = (linea[6:linea.find('(')])
                auxlen = len(auxcad) + 7
                auxcad = auxcad + " "
                auxcad = auxcad + linea[auxlen:linea.find(')')]
                name.append(auxcad)
        #Agrega el "->"        
        for i in name:
            temp = i[0:i.find(' ')]
            auxlen = len(temp) + 1 #Aquí se coloca despues del " "_
            auxtemp = i[auxlen:50]
            if auxtemp == "":
                pass
            else:
                importStrings = (temp + "->" + auxtemp)
                print(importStrings)
        self.relaciones = importStrings
        return importStrings

    def __str__(self):
        st = ""
        for s in self.clases:
            st += s.__str__()
        st += self.relaciones
        return st

#Primero obtener los archivos
#Despues buscar las clases
#Las funciones de las clases
#Las relaciones de las clases
#Información en: https://plantuml.com/class-diagram

#El programa genera un txt
#Ese txt se manda a plantuml
#Finalmente se muestra el diagrama

Plant = GeneradorPlantUMLTxt()
Plant.leerArchivoaClase("Prueba.py")
print(Plant)

#Esta parte crea el .png y lo abre
#os.system("java -jar plantuml.jar salida.txt") # Termine sin error
#os.system("xviewer Clases.png") # Archivo existe
