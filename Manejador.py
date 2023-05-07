from claseViajero import Viajero

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []
   
    def cargarViajero(self,num,dni,nom,ap,millas):
 
        newViajero = Viajero(num, dni, nom, ap, int(millas))
        self.__lista.append(newViajero)

        
    #Muestro todos los viajeros
    def showViajeros(self):
        print("Viajero con mayor cantidad de millas ")
        print('{} {} {} {} {}'.format('Numer','Documento','Nombre','Apellido','Millas'))
        for Viajero in self.__lista:
            num = Viajero.getNumero()
            dni = Viajero.getDocumento()
            nom = Viajero.getNombre()
            ap = Viajero.getApellido()
            millas= Viajero.getMillas()
            
        print ('{} {} {} {} {}'.format(num,dni,nom,ap,millas))    


    def sumar_millas(self):
        acum=0
        for Viajero in self.__lista:

            acum +=Viajero.getMillas()

        print("Acumulador total de millas es: {}".format(acum))


    def compara(self,num,dni,nom,ap,millas,xnumero):

        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas = int(millas)

        i=0
        encontrado = False

        while i < len(self.__lista) and not encontrado:
            if self.__lista[i] == xnumero:
                encontrado=True
            else:
                i+=1
        pos = i    
        return pos

    def canjear_millas(self, millas_a_canjear):
        millas_actuales = self.__millas
        if millas_a_canjear <= millas_actuales:
            self.__millas -= int(millas_a_canjear)
            print(f"{self.__millas} millas canjeadas correctamente. Millas restantes: {millas_a_canjear}.")
        else:
            print("No hay suficientes millas disponibles para canjear.")
        return self
