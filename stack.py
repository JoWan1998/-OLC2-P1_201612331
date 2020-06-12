
class pila:
    def __init__(self):
        self.pila = []

    def insertPila(self,pila):
        self.pila.append(pila)

    def getValor(self,direccion):
        for vpilas in self.pila:
            if vpilas.direccion == direccion:
                return vpilas.valor

        return None

    def updatePila(self,direccion,valor):
        for vpilas in self.pila:
            if vpilas.direccion == direccion:
                vpilas.valor = valor
                return True

        print("Exception Error: No Existe la direccion de pila: "+direccion)
        return False

    def deletePila(self,direccion):
        pos = None
        for vpilas in self.pila:
            if vpilas.direccion == direccion:
                pos = vpilas
                break

        if pos != None:
            self.pila.remove(pos)
            return True

        print("Exception Error: No Existe la direccion de pila: " + direccion)
        return False

class vpila:
    def __init__(self,valor,direccion):
        self.direccion = direccion
        self.valor = valor