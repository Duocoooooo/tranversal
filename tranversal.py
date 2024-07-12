from os import system
system("cls")
from funciones import *
#########################################################################################################################################
diccionario_de_trabajadores = {"nombre": "Juan Pérez", "sueldo": 300001,
                               "nombre":  "María García", "sueldo": 300002,
                               "nombre":  "Carlos López", "sueldo": 300003,
                               "nombre":  "Ana Martínez", "sueldo": 300004, 
                               "nombre":  "Pedro Rodríguez", "sueldo": 300005,
                               "nombre":  "Laura Hernández", "sueldo": 300006,
                               "nombre":  "Miguel Sánchez", "sueldo": 300007,
                               "nombre":  "Isabel Gómez", "sueldo": 300008,
                               "nombre":  "Francisco Díaz", "sueldo": 300009,
                               "nombre":  "Elena Fernández", "sueldo": 300010}
#########################################################################################################################################
def random_sueldo():
    print(diccionario_de_trabajadores)

    #for clave in diccionario_de_trabajadores:
        #for valor in clave:
            #print("clave: ", clave, "valor: ", valor)
#########################################################################################################################################
def sueldos_clasificados():
    lista_clasificada = []
    for i in trabajadores_lista:
        for sueldo in i:
            if sueldo < 800000:
                lista.append(sueldo)
#########################################################################################################################################
def estadisticas():
    print("estadisticas")
#########################################################################################################################################
def reporte():
    print("reporte")
#########################################################################################################################################
def despedida():
    print("""Finalizando programa…
#Desarrollado por Jorge Cisternas
#RUT 20.301.147-4""")
#########################################################################################################################################
boleano = True
while boleano == True:
    input("accion")
    print("""menu:
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa""")
    eleccion = input("eleccion: ")

    if eleccion == "1":
        random_sueldo()
        
        #try:
            #random_sueldo()
        #except:
            #print("mmmmm, estamos trabajando en una solucion para usted")
    elif eleccion == "2":
        try:
            sueldos_clasificados()
        except:
                print("mmmmm, estamos trabajando en una solucion para usted")
    elif eleccion == "3":
        try:
            estadisticas()
        except:
                print("mmmmm, estamos trabajando en una solucion para usted")
    elif eleccion == "4":
        try:
            reporte()
        except:
            print("mmmmm, estamos trabajando en una solucion para usted")
    elif eleccion == "5":
        print("""Finalizando programa…
#Desarrollado por Jorge Cisternas
#RUT 20.301.147-4""")
        break
    else:
        print("opcion no valida")
#########################################################################################################################################

