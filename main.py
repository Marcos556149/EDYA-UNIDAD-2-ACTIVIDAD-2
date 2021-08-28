from ClasePila import Pila
def convertir(numD):
    guardarNum=numD
    a=''
    unaPila=Pila()
    while numD != 0:
        if (numD % 2) == 1:
            unaPila.insertar(1)
        else:
            unaPila.insertar(0)
        numD //=2
    while (unaPila.vacia() == False):
        a+=str(unaPila.suprimir())
    print("La representacion en binario del numero {} es: {}".format(guardarNum,a))
if __name__=='__main__':
    print("----CONVERSION DE DECIMAL A BINARIO----")
    num= int(input("Ingrese el numero decimal: "))
    convertir(num)


