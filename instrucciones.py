#definicion de clases para implementacion de AUGUS
#Jose Wannan @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from AST import Nodo
from TablaSimbolos import *
from enumeradores import *

class instruccion:
    def information(self):

        self.information = "instruccion of augus"

class etiqueta(instruccion):

    def __init__(self,enum,nombre,linea, instrucciones=[],principal=False):
        self.tipo_intruccion = enum
        self.nombre = nombre
        self.linea = linea
        self.instruccionesd = instrucciones
        self.principal = principal

    def implements(self,ts,pila,instrucciones):
        try:

            for intruccion in self.instruccionesd:
                if isinstance(intruccion,asignacion):
                    intruccion.implements(ts,pila,instrucciones)
                elif isinstance(intruccion,destructor):
                    intruccion.implements(ts,pila,instrucciones)
                elif isinstance(intruccion,imprimir):
                    intruccion.implements(ts,pila,instrucciones)
                elif isinstance(intruccion,etiqueta):
                    md =  intruccion.implements(ts,pila,instrucciones)
                    if md == 1:
                        return 1
                elif isinstance(intruccion,sentencia_control):
                    md = intruccion.implements(ts,pila,instrucciones)
                    if md == 1:
                        return 1
                elif isinstance(intruccion,salto_bandera):
                    md = intruccion.implements(ts,pila,instrucciones)
                    if md ==1 :
                        return 1
                elif isinstance(intruccion,salida):
                    return 1
            return 0
        except:
            return -1

class salto_bandera(instruccion):

    def __init__(self, enum, bandera,linea):
        self.tipo_instruccion = enum
        self.bandera = bandera
        self.linea = linea

    def implements(self,ts,pila,instrucciones):
        for inst in instrucciones:
            if isinstance(inst,etiqueta):
                if inst.nombre == self.bandera:
                    md = inst.implements(ts,pila,instrucciones)
                    if md == 1:
                        return 1

        return 0

class asignacion(instruccion):

    def __init__(self,enum,linea,variable,valor,pos=-1):
        self.tipo_instruccion = enum
        self.linea = linea
        self.variable = variable
        self.valor = valor
        self.pos = pos

    def implements(self,ts,pila,instrucciones):
        try:
            simbol = ts.getSimbolo(self.variable,pila)
            if self.pos == -1:
                if simbol == None:
                    value = self.valor.get_Value(ts,pila)
                    if value != None:
                        if isinstance(value,simbolo):
                            tipo = self.variable[0:1]
                            registro = None
                            if tipo == 't':
                                registro = REGISTRO.TEMPORAL
                            elif tipo == 'a':
                                registro = REGISTRO.PARAMETRO
                            elif tipo == 'v':
                                registro = REGISTRO.FUNCION
                            elif tipo == 'r':
                                registro = REGISTRO.RA
                            elif tipo == '&':
                                registro = REGISTRO.APUNTADOR
                                self.variable = self.variable[1:]
                            elif tipo == 's':
                                tipo = self.variable[1:2]
                                if tipo == 'p':
                                    registro = REGISTRO.APUNTADORPILA
                                else:
                                    registro = REGISTRO.PILA

                            if registro == REGISTRO.APUNTADOR or registro == REGISTRO.APUNTADORPILA:
                                simbol = ts.getPuntero(value.valor,pila)
                                if simbol !=None:
                                    simbolito = simbolo(self.variable, simbol.direccion, TYPE_VALUE.APUNTADOR, registro)
                                    ts.insertSimbolo(simbolito,pila)
                                else:
                                    simbol = ts.getpilaApuntada1(self.valor.value,pila)
                                    if simbol.valor != None:
                                        simbolito = simbolo(self.variable, simbol.direccion, TYPE_VALUE.APUNTADOR,registro)
                                        ts.insertSimbolo(simbolito, pila)
                            elif registro == REGISTRO.PILA:
                                simbolito = simbolo(self.variable, value.valor, value.tipo, registro)
                                ts.insertPila(simbolito,value.valor,pila)
                            else:
                                simbolito = simbolo(self.variable, value.valor, value.tipo, registro)
                                ts.insertSimbolo(simbolito,pila)
                        else:
                            tipo = self.variable[0:1]
                            registro = None
                            if  tipo == 't':
                                registro = REGISTRO.TEMPORAL
                            elif tipo == 'a':
                                registro = REGISTRO.PARAMETRO
                            elif tipo == 'v':
                                registro = REGISTRO.FUNCION
                            elif tipo == 'r':
                                registro = REGISTRO.RA
                            elif tipo == '&':
                                registro = REGISTRO.APUNTADOR
                                self.variable = self.variable[1:]
                            elif tipo == 's':
                                tipo = self.variable[1:2]
                                if tipo == 'p':
                                    registro = REGISTRO.APUNTADORPILA
                                else:
                                    registro = REGISTRO.PILA
                            try:
                                if registro == registro.APUNTADORPILA:
                                    simbol = ts.getPuntero(value['valor'], pila)
                                    simbolito = simbolo(self.variable, simbol.direccion, TYPE_VALUE.APUNTADOR,registro)
                                    ts.insertSimbolo(simbolito, pila)
                                elif value['method'] == 'apuntador':
                                    simbol = ts.getPuntero(value['valor'],pila)
                                    simbolito = simbolo(self.variable,simbol.direccion,TYPE_VALUE.APUNTADOR,registro)
                                    ts.insertSimbolo(simbolito,pila)
                                elif registro == REGISTRO.PILA:
                                    simbolito = simbolo(self.variable, value['valor'], value['tipo'], registro)
                                    ts.insertPila(simbolito, value['valor'], pila)
                                else:
                                    simbolito = simbolo(self.variable, value['valor'], value['tipo'], registro)
                                    ts.insertSimbolo(simbolito,pila)
                            except:
                                print("ERROR, Uncaugth error in line: "+str(self.linea))
                    else:
                        print('Semantic Error, No se puede asignar el valor a la variable, es probable no exista, linea: '+str(self.linea))
                else:
                    value = self.valor.get_Value(ts,pila)
                    vl = False
                    if isinstance(value, simbolo):

                        if value.registro == REGISTRO.APUNTADORPILA:
                            value = ts.getpilaApuntada(value.valor,pila)
                            if simbol.tipo != TYPE_VALUE.ARREGLO and simbol.tipo != TYPE_VALUE.APUNTADOR:
                                vl = ts.update(self.variable, value.valor,value.tipo)
                            elif simbol.tipo == TYPE_VALUE.ARREGLO:
                                vl = ts.update(self.variable, value.valor,value.tipo)
                            elif simbol.tipo == TYPE_VALUE.APUNTADOR:
                                vl = ts.updatePuntero(self.variable, value.valor, pila)
                        else:
                            if simbol.tipo != TYPE_VALUE.ARREGLO and simbol.tipo != TYPE_VALUE.APUNTADOR:
                                vl = ts.update(self.variable, value.valor,value.tipo)
                            elif simbol.tipo == TYPE_VALUE.ARREGLO:
                                vl = ts.update(self.variable, value.valor,value.tipo)
                            elif simbol.tipo == TYPE_VALUE.APUNTADOR:
                                vl = ts.updatePuntero(self.variable, value.valor, pila)
                    else:
                        if simbol.tipo != TYPE_VALUE.ARREGLO and simbol.tipo != TYPE_VALUE.APUNTADOR:
                            vl = ts.update(self.variable, value['valor'],value['tipo'])
                        elif simbol.tipo == TYPE_VALUE.ARREGLO:
                            vl = ts.update(self.variable,value['valor'],value['tipo'])
                        elif simbol.tipo == TYPE_VALUE.APUNTADOR:
                            vl =ts.updatePuntero(self.variable, value['valor'],pila)

                    if not vl:
                        print("Uncaught Error, La operacion no puede actualizarse o definirse, en la linea: "+str(self.linea))
            else:
                if simbol == None:
                    if isinstance(self.pos,list):
                        value = self.valor.get_Value(ts, pila)
                        if isinstance(value,simbolo):
                            lis = self.insertInArray(ts,{},self.pos,value.valor,pila)
                            simbolito = simbolo(self.variable,lis,TYPE_VALUE.ARREGLO,REGISTRO.TEMPORAL)
                            ts.insertSimbolo(simbolito,pila)
                        elif isinstance(value,dict):
                            lis = self.insertInArray(ts, {}, self.pos, value['valor'], pila)
                            simbolito = simbolo(self.variable, lis, TYPE_VALUE.ARREGLO, REGISTRO.TEMPORAL)
                            ts.insertSimbolo(simbolito, pila)
                    else:
                        print("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea))
                else:
                    if simbol.tipo == TYPE_VALUE.ARREGLO:
                        if isinstance(self.pos,list):
                            value = self.valor.get_Value(ts, pila)
                            if simbol.valor == None: simbol.valor = {}
                            if isinstance(value,simbolo):
                                lis = self.insertInArray(ts,simbol.valor,self.pos,value.valor,pila)
                                ts.update(simbol.id, lis)
                            elif isinstance(value,dict):
                                lis = self.insertInArray(ts,simbol.valor, self.pos, value['valor'], pila)
                                ts.update(simbol.id, lis)
                        else:
                            print("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea))
                    else:
                        print("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea))

        except:
            print("Uncaught Error, La operacion no puede completarse o definirse, en la linea: "+str(self.linea))

    def setList(self,ts,dictt,valor,pila,pos,cont):
        cont -= 1
        el = next(pos)
        vl = el.get_Value(ts, pila)
        if cont ==0:
            if isinstance(vl,simbolo):
                if vl.valor in dictt:
                    dictt[vl.valor] = (valor)
                else:
                    dictt[vl.valor] = (valor)
                return dictt
            elif isinstance(vl,dict):
                if vl['valor'] in dictt:
                    dictt[vl['valor']] = (valor)
                else:
                    dictt[vl['valor']] = (valor)
                return dictt
        else:
                if isinstance(vl, simbolo):
                    if vl.valor in dictt:
                        dictt[vl.valor] = (self.setList(ts, dictt[vl.valor], valor, pila, pos, cont))
                    else:
                        dictt[vl.valor] = (self.setList(ts, {}, valor, pila, pos, cont))
                    return dictt
                elif isinstance(vl, dict):
                    if vl['valor'] in dictt:
                        dictt[vl['valor']] = (self.setList(ts, dictt[vl['valor']], valor, pila, pos, cont))
                    else:
                        dictt[vl['valor']] = (self.setList(ts, {}, valor, pila, pos, cont))
                    return dictt


    def insertInArray(self,ts,lists,pos,valor,pila):
        try:
            con = len(pos)
            con -= 1
            posi = iter(pos)
            mm = next(posi)
            vl = mm.get_Value(ts, pila)
            if con > 0:
                if isinstance(vl, simbolo):
                    if vl.valor in lists:
                        m = lists[vl.valor]
                        if isinstance(m,str):
                            if con == 1:
                                lists[vl.valor] = (self.strlist(ts, lists[vl.valor], valor, pila, posi))
                        else:
                            lists[vl.valor] = (self.setList(ts, lists[vl.valor], valor, pila, posi, con))
                    else:
                        lists[vl.valor] = (self.setList(ts, {}, valor, pila, posi, con))
                    return lists
                elif isinstance(vl, dict):
                    if vl['valor'] in lists:
                        m = lists[vl['valor']]
                        if isinstance(m, str):
                            if con == 1:
                                lists[vl['valor']] = (self.strlist(ts, lists[vl['valor']], valor, pila, posi))
                        else:
                            lists[vl['valor']] = (self.setList(ts, lists[vl['valor']], valor, pila, posi, con))
                    else:
                        lists[vl['valor']] = (self.setList(ts, {}, valor, pila, posi, con))
                    return lists
            else:
                if isinstance(vl, simbolo):
                    lists[vl.valor] =  valor
                    return lists
                elif isinstance(vl, dict):
                    lists[vl['valor']] =  valor
                    return lists
        except:
            return None

    def strlist(self,ts,lists,valor,pila,posi):
        el = next(posi)
        vl = el.get_Value(ts, pila)
        kls = list(lists)
        if isinstance(vl,simbolo):
            if isinstance(vl.valor,int) or isinstance(vl.valor,float):
                vl.valor = int(vl.valor)
                if (len(kls)-1) < vl.valor:
                    value = ''
                    for nn in kls:
                        value += nn
                    c = len(kls)
                    if (vl.valor) > c:
                        for a in range((vl.valor)):
                            if a >= c:
                                value += ' '
                    value += valor
                    lists = value
                    return lists
                else:
                    kls[vl.valor] = valor
        elif isinstance(vl,dict):
            if isinstance(vl['valor'], int) or isinstance(vl['valor'], float):
                vl.valor = int(vl['valor'])
                if  (len(kls)-1) < vl['valor']:
                    value = ''
                    for nn in kls:
                        value += nn
                    c = len(kls)
                    if (vl['valor']) > c:
                        for a in range((vl['valor'])):
                            if a >= c:
                                value += ' '
                    value += valor
                    lists = value
                    return lists
                else:
                    kls[vl['valor']] = valor

        value = ''
        for nn in kls:
            value += nn
        lists = value
        return lists

class sentencia_control(instruccion):

    def __init__(self,enum,linea,condicion,bandera):
        self.tipo_instruccion = enum
        self.condicion = condicion
        self.bandera = bandera
        self.linea = linea

    def implements(self,ts,pila,instrucciones):
        try:
            pasd = self.condicion.get_Value(ts,pila)
            pp = -1
            if isinstance(pasd,simbolo): pp = pasd.valor
            elif isinstance(pasd,dict): pp = pasd['valor']

            if pp == 1:
                for ins in instrucciones:
                    if isinstance(ins, etiqueta):
                        if ins.nombre == self.bandera:
                            md = ins.implements(ts, pila, instrucciones)
                            if md == 1:
                                return 1

                return 0
        except:
            print("Error Desconocido en la linea: "+str(self.linea))

class destructor(instruccion):

    def __init__(self,enum,linea,variable):
        self.tipo_instruccion = enum
        self.variable = variable
        self.linea = linea

    def implements(self,ts,pila,instrucciones):
        id = self.variable.get_Value(ts,pila)
        if isinstance(id,simbolo):
            ts.destruir(id.id)
        elif isinstance(id,dict):
            ts.destruir(id['valor'])

class imprimir(instruccion):

    def __init__(self,enum,linea,valor):
        self.tipo_instruccion = enum
        self.valor = valor
        self.linea = linea

    def implements(self,ts,pila,instrucciones):
        try:
            vl = self.valor.get_Value(ts,pila)
            if isinstance(vl,simbolo):
                if vl.valor == '\\n':
                    print('')
                else:
                    if isinstance(vl.valor,str): vl.valor = vl.valor.replace('\\n','')
                    print(vl.valor)
            elif isinstance(vl,dict):
                if vl['valor'] == '\\n':
                    print('')
                else:
                    if isinstance(vl['valor'], str): vl['valor'] = vl['valor'].replace('\\n', '')
                    print(vl['valor'])
        except:
            print("Error Inesperado, no se puede imprimir el valor, linea: "+str(self.linea))

class salida(instruccion):

    def __init__(self,enum,linea):
        self.tipo_instruccion = enum
        self.linea = linea

    def implements(self,ts,pila,instrucciones):
        print("Adios")


