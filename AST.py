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
        self.production = ''
        self.rule = ''

    def addHijo(self,Nodo):
        self.hijos.append(Nodo)

    def produccion(self,produccion):
        self.production = produccion

    def reglaSemantica(self,regla):
        self.rule = regla

    def createReglaS(self,padre,file,cont):
        data =''
        if padre.production != '' and cont ==0:
            data += '<TR><TD> '+padre.value+' </TD><TD> '+padre.production+' </TD><TD> '+padre.rule+' </TD></TR>\n'
            for p in padre.hijos:
                data += '<TR><TD> ' + p.value + ' </TD><TD> ' + p.production + ' </TD><TD> ' + p.rule + ' </TD></TR>\n'
                file.write(data)
                self.createReglaS(p,file,cont+1)
        elif padre.production != '':
            for p in padre.hijos:
                if p.production != '':
                    data += '<TR><TD> ' + p.value + ' </TD><TD> ' + p.production + ' </TD><TD> ' + p.rule + ' </TD></TR>\n'
                    file.write(data)
                    self.createReglaS(p,file,cont+1)


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



