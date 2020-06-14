#CLASE AST - ARBOL DE SINTAXIS ABSTRACTA, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA


#clase para la generacion de nodos pertenecientes,
#raiz->hijo,hijo
#raiz->hijo
class Nodo:
    def __init__(self,valor):
        self.value = valor
        self.hijos = []
        self.data = ''

    def addHijo(self,Nodo):
        self.hijos.append(Nodo)

    def getData(self,padre,cont,file):
        data = ''
        for p in padre.hijos:
            data += 'Nodo_'+str(cont)+'[label=\"'+padre.value+'\"];\n'
            data +=  padre.value+'_'+str(cont)+'[label=\"'+p.value+'\"];\n'
            data += 'Nodo_'+str(cont)+'->'+padre.value+'_'+str(cont)+';\n'
            file.write(data)
            if len(p.hijos) >0:
                self.getData(p,cont,file)
                cont +=1

        print(data)



