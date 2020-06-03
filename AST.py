#CLASE AST - ARBOL DE SINTAXIS ABSTRACTA, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA


#clase para la generacion de nodos pertenecientes,
#raiz->hijo,hijo
#raiz->hijo
class Nodo:
    def __init__(self,valor):
        self.value = valor
        self.hijos = list()

    def addHijo(self,Nodo):
        self.hijos.append(Nodo)
