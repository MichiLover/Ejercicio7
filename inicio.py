import csv
from claseViajero import Viajero
from Manejador import Manejador

if __name__== '__main__':
    print("EJERCICIO 1")
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=',')
    newViajero= Manejador()
    bandera = True

    for fila in reader:
        if bandera:
            bandera = False
        else:
             print("\n")
             print("Datos del archivo cargado")
             numero=int(fila[0])
             documento=fila[1]
             nombre=fila[2]
             apellido=fila[3]
             millas=int(fila[4])
             print("\n")
             newViajero.cargarViajero(numero, documento, nombre, apellido, millas)
    archivo.close()
    print("EJERCICIO 1")
    xnum = int(input ("Ingresar un numero de viajero: "))
    viajero1 = Viajero(xnum,documento,nombre,apellido, fila[4])
    if viajero1 == 5000:
        print('El viajero tiene 5000 millas acumuladas.')
    else:
        print("Las millas son diferentes")
    print("\n")
    print("--------------------------------------------------------------------------------------------")
    print("EJERCICIO 2")
    newViajero.sumar_millas()
    print("--------------------------------------------------------------------------------------------")
    print("EJERCICIO 3")
    xnumero = int(input ("Ingresar un numero de viajero: "))
    resp=newViajero.compara(numero,documento,nombre,apellido,millas,xnumero)
    if resp != None:
        millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
        viajero2 = Viajero(xnumero,documento,nombre,apellido, millas)
        viajero2 = millas_a_canjear - viajero2
        newViajero.canjear_millas(viajero2)
    else:
        print("El número de viajero ingresado no existe.")

print("--------------------------------------------------------------------------------------------")
