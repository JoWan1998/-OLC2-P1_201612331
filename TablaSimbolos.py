from pila import *
class ts:
    def __init__(self):
        self.simbolos = []

    def getValue(self,id):
        for simbolito in self.simbolos:
            if simbolito.id == id:
                return simbolito.valor
        return None

    def getValueDirection(self,id):
        for simbolito in self.simbolos:
            if simbolito.id == id:
                return simbolito.direccion
        return None

    def insertSimbolo(self,simbolo):
        count = 0
        for simbolito in self.simbolos:
            count +=1
        count +=1
        simbolo.direccion = hex(count)
        self.simbolos.append(simbolo)

    def insertPuntero(self,simbolo):
        count = 0
        for simbolito in self.simbolos:
            count +=1
        count +=1
        simbolo.direccion = hex(count)
        self.simbolos.append(simbolo)

    def insertPila(self,simbolo,valor,pila):
        count = 0
        for simbolito in self.simbolos:
            count +=1
        count +=1
        simbolo.direccion = hex(count)
        cant = 0
        for pilita in pila:
            cant +=1
        directionpila = hex(cant)
        pilas = vpila(valor,directionpila)
        simbolo.valor = directionpila
        pila.append(pilas)
        self.simbolos.append(simbolo)


    def getSimbolo(self,id):
        for simbolito in self.simbolos:
            if simbolito.id == id:
                return simbolito
        return None



    def update(self,id,valor):
        for simbolo in self.simbolos:
            if simbolo.id == id:
                simbolo.valor = valor
                return

        print("no existe la variable: "+id)



class simbolo:
    def __init__(self,id,valor,tipo,registro):
        self.id = id
        self.valor = valor
        self.direccion = 0x000
        self.tipo = tipo
        self.registro = registro