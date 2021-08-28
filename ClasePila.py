from ClaseNodo import Nodo
class Pila:
    __cant=0
    __tope=None
    def __init__(self):
        self.__tope = None
    def vacia(self):
        return self.__cant == 0
    def insertar(self,x):
        nodo= Nodo(x)
        nodo.setSiguiente(self.__tope)
        self.__tope= nodo
        self.__cant += 1
        return x
    def suprimir(self):
        if self.vacia():
            print("Pila Vacia")
        else:
            guaradarTope= self.__tope
            self.__tope= self.__tope.getSiguiente()
            self.__cant -= 1
            return guaradarTope.getDato()
    def mostrar(self):
        guardarTope= self.__tope
        while guardarTope != None:
            print(guardarTope.getDato())
            guardarTope= guardarTope.getSiguiente()

