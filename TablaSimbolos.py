from stack import *
from enumeradores import *
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

    def insertSimbolo(self,simbolo,pila):
        count = 0
        for simbolito in self.simbolos:
            count +=1
        count +=1
        simbolo.direccion = hex(count)
        self.simbolos.append(simbolo)

    def insertPunteropila(self,simbolo,pila):
        count = 0
        for simbolito in self.simbolos:
            count +=1
        count +=1
        simbolo.direccion = hex(count)
        self.simbolos.append(simbolo)

    def insertPuntero(self,simbolo,pila):
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
        for pilita in pila.pila:
            cant +=1
        cant +=1
        directionpila = hex(cant)
        pilas = vpila(valor,directionpila)
        simbolo.valor = directionpila
        pila.insertPila(pilas)
        self.simbolos.append(simbolo)


    def getSimbolo(self,id,pila):
        for simbolito in self.simbolos:
            if simbolito.id == id:
                if simbolito.registro == REGISTRO.PILA:
                    vals = pila.getValor(simbolito.valor)
                    if vals != None:
                        simbol = simbolo(simbolito.id,vals,simbolito.tipo,REGISTRO.TEMPORAL)
                        return simbol
                else:
                    return simbolito
        return None

    def getpilaApuntada1(self,id,pila):
        for simbolito in self.simbolos:
            if simbolito.id == id:
                return simbolito
        return None
    def getpilaApuntada(self,direccion,pila):
        for simbolito in self.simbolos:
            if simbolito.direccion == direccion:
                vm = pila.getValor(simbolito.valor)
                sim = simbolo(simbolito.id,vm,simbolito.tipo,simbolito.registro)
                return sim
        return None

    def getPuntero(self,direccion,pila):
        for simbolito in self.simbolos:
            if simbolito.direccion == direccion:
                if simbolito.registro == REGISTRO.APUNTADORPILA:
                    vals = pila.getValor(simbolito.valor)
                    if vals != None:
                        simboret = simbolo(simbolito.id,vals,simbolito.tipo,simbolito.registro)
                        return simboret
                else:
                    return simbolito
        return None

    def update(self,id,valor):
        for simbolo in self.simbolos:
            if simbolo.id == id:
                simbolo.valor = valor
                return True

        print("no existe la variable: "+id)
        return False

    def updatePunteroPila(self,id,valor,pila):
        for simbolo in self.simbolos:
            if simbolo.id == id:
                val = pila.updatePila(simbolo.valor,valor)
                return val

        print("no existe la variable: "+id)
        return False

    def updatePuntero(self,id,valor,pila):
        for simbolo in self.simbolos:
            if simbolo.id == id:
                for simbolito in self.simbolos:
                    if simbolito.direccion == simbolo.valor:
                        if simbolito.registro == REGISTRO.PILA:
                            print(valor)
                            self.updatePunteroPila(simbolito.id,valor,pila)
                        else:
                            simbolito.valor = valor
                        return True

        print("no existe la variable: "+id)
        return False

class simbolo:
    def __init__(self,id,valor,tipo,registro):
        self.id = id
        self.valor = valor
        self.direccion = 0x000
        self.tipo = tipo
        self.registro = registro