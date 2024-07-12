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
