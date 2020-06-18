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

    def implements(self,ts,pila,instrucciones,file,linea=-1):
        ln = 0
        try:
            if linea != -1:
                linea += self.instruccionesd[0].linea
                for intruccion in self.instruccionesd:

                    if isinstance(intruccion,asignacion):
                        if intruccion.linea == linea:
                            return 2
                        else:
                            intruccion.implements(ts, pila, instrucciones,file)
                    elif isinstance(intruccion,destructor):
                        if intruccion.linea == linea:
                            return 2
                        else:
                            intruccion.implements(ts, pila, instrucciones,file)
                    elif isinstance(intruccion,imprimir):
                        if intruccion.linea-2 == linea or intruccion.linea-1 == linea:
                            return 2
                        else:
                            intruccion.implements(ts, pila, instrucciones,file)
                    elif isinstance(intruccion,etiqueta):
                        if intruccion.linea == linea:
                            return 2
                        else:
                            md = intruccion.implements(ts, pila, instrucciones, file,linea)
                            if md in (1, 2):
                                return 1
                            elif md < 0:
                                return -1
                    elif isinstance(intruccion,sentencia_control):
                        if intruccion.linea == linea:
                            return 2
                        else:
                            md = intruccion.implements(ts, pila, instrucciones,file)
                            if md in (1, 2):
                                return 1
                            elif md < 0:
                                return -1
                    elif isinstance(intruccion,salto_bandera):
                        if intruccion.linea == linea:
                            return 2
                        else:
                            md = intruccion.implements(ts, pila, instrucciones,file)
                            if md in(1,2):
                                return 1
                            elif md < 0:
                                return -1
                    elif isinstance(intruccion,salida):
                        return 1
                return 1
            else:
                for intruccion in self.instruccionesd:
                    ln = intruccion.linea
                    if isinstance(intruccion,asignacion):
                        intruccion.implements(ts,pila,instrucciones,file)
                    elif isinstance(intruccion,destructor):
                        intruccion.implements(ts,pila,instrucciones,file)
                    elif isinstance(intruccion,imprimir):
                        intruccion.implements(ts,pila,instrucciones,file)
                    elif isinstance(intruccion,etiqueta):
                        md =  intruccion.implements(ts,pila,instrucciones,file)
                        if md == 1:
                            return 1
                        elif md <0:
                            file.write("Excepcion llamada, en la instruccion: "+intruccion.nombre+", linea: "+str(intruccion.linea)+"\n")
                            return -1
                    elif isinstance(intruccion,sentencia_control):
                        md = intruccion.implements(ts,pila,instrucciones,file)
                        if md == 1:
                            return 1
                        elif md < 0:
                            file.write("Excepcion llamada, en la sentencia if, linea: "+str(intruccion.linea)+"\n")
                            return -1
                    elif isinstance(intruccion,salto_bandera):
                        md = intruccion.implements(ts,pila,instrucciones,file)
                        if md ==1 :
                            return 1
                        elif md < 0:
                            file.write("Excepcion llamada, en la sentencia goto, linea: " + str(intruccion.linea)+"\n")
                            return -1
                    elif isinstance(intruccion,salida):
                        return 1
                return 1
        except Exception as e:
            print(e)
            file.write("Ah ocurrido una Excepcion. Metodo: "+self.nombre+", en la linea: "+str(ln)+"\n")
            return -1

class salto_bandera(instruccion):

    def __init__(self, enum, bandera,linea):
        self.tipo_instruccion = enum
        self.bandera = bandera
        self.linea = linea

    def implements(self,ts,pila,instrucciones,file):
        try:
            for inst in instrucciones:
                if isinstance(inst,etiqueta):
                    if inst.nombre == self.bandera:
                        md = inst.implements(ts,pila,instrucciones,file)
                        if md == 1:
                            return 1
                        else:
                            return -1

            return 0
        except:
            file.write("Error, stack overflow, unset the var, en linea: "+self.linea+'\n')
            return -1

class asignacion(instruccion):

    def __init__(self,enum,linea,variable,valor,pos=-1):
        self.tipo_instruccion = enum
        self.linea = linea
        self.variable = variable
        self.valor = valor
        self.pos = pos

    def implements(self,ts,pila,instrucciones,file):
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
                            except Exception as e:
                                print(e)
                                print("ERROR, Uncaugth error in line: " + str(self.linea))
                                file.write("ERROR, Uncaugth error in line: "+str(self.linea)+'\n')
                    else:
                        print(
                            'Semantic Error, No se puede asignar el valor a la variable, es probable no exista, linea: ' + str(
                                self.linea)+'\n')
                        file.write('Semantic Error, No se puede asignar el valor a la variable, es probable no exista, linea: '+str(self.linea)+'\n')
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
                        file.write("Uncaught Error, La operacion no puede actualizarse o definirse, en la linea: "+str(self.linea)+'\n')
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
                        file.write("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea)+'\n')
                else:
                    if simbol.tipo == TYPE_VALUE.ARREGLO:
                        if isinstance(self.pos,list):
                            value = self.valor.get_Value(ts, pila)
                            if simbol.valor == None: simbol.valor = {}
                            if isinstance(value,simbolo):
                                lis = self.insertInArray(ts,simbol.valor,self.pos,value.valor,pila)
                                ts.update(simbol.id, lis,simbol.tipo)
                            elif isinstance(value,dict):
                                lis = self.insertInArray(ts,simbol.valor, self.pos, value['valor'], pila)
                                ts.update(simbol.id, lis,simbol.tipo)
                        else:
                            print("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea))
                            file.write("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea)+'\n')
                    else:
                        print("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea))
                        file.write("Uncaugth Error, no ha podido asignar el arreglo, linea: " + str(self.linea)+'\n')

        except Exception as e:
            print(e)
            print("Uncaught Error, La operacion no puede completarse o definirse, en la linea: " + str(self.linea)+"\n")
            file.write("Uncaught Error, La operacion no puede completarse o definirse, en la linea: "+str(self.linea)+'\n')

    def setList(self,ts,dictt,valor,pila,pos,cont):
        try:
            cont -= 1
            el = next(pos)
            vl = el.get_Value(ts, pila)
            if cont ==0:
                if isinstance(vl,simbolo):
                    if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                    if vl.valor in dictt:
                        dictt[vl.valor] = (valor)
                    else:
                        dictt[vl.valor] = (valor)
                    return dictt
                elif isinstance(vl,dict):
                    if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                    if vl['valor'] in dictt:
                        dictt[vl['valor']] = (valor)
                    else:
                        dictt[vl['valor']] = (valor)
                    return dictt
            else:
                    if isinstance(vl, simbolo):
                        if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                        if vl.valor in dictt:
                            dictt[vl.valor] = (self.setList(ts, dictt[vl.valor], valor, pila, pos, cont))
                        else:
                            dictt[vl.valor] = (self.setList(ts, {}, valor, pila, pos, cont))
                        return dictt
                    elif isinstance(vl, dict):
                        if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                        if vl['valor'] in dictt:
                            dictt[vl['valor']] = (self.setList(ts, dictt[vl['valor']], valor, pila, pos, cont))
                        else:
                            dictt[vl['valor']] = (self.setList(ts, {}, valor, pila, pos, cont))
                        return dictt
        except Exception as e:
            val = str(e)
            print(val)
            return None

    def insertInArray(self,ts,lists,pos,valor,pila):
        try:
            con = len(pos)
            con -= 1
            posi = iter(pos)
            mm = next(posi)
            vl = mm.get_Value(ts, pila)
            if con > 0:
                if isinstance(vl, simbolo):
                    if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
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
                    if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
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
                    if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                    lists[vl.valor] =  valor
                    return lists
                elif isinstance(vl, dict):
                    if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                    lists[vl['valor']] =  valor
                    return lists
        except Exception as e:
            print(e)
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
                vl['valor'] = int(vl['valor'])
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

    def implements(self,ts,pila,instrucciones,file):
        try:
            pasd = self.condicion.get_Value(ts,pila)
            pp = -1
            if isinstance(pasd,simbolo): pp = pasd.valor
            elif isinstance(pasd,dict): pp = pasd['valor']

            if pp == 1:
                for ins in instrucciones:
                    if isinstance(ins, etiqueta):
                        if ins.nombre == self.bandera:
                            md = ins.implements(ts, pila, instrucciones,file)
                            if md == 1:
                                return 1
                            else:
                                return md

            return 0
        except Exception as e:
            print(e)
            file.write("Error Desconocido en la linea: "+str(self.linea)+'\n')

class destructor(instruccion):

    def __init__(self,enum,linea,variable):
        self.tipo_instruccion = enum
        self.variable = variable
        self.linea = linea

    def implements(self,ts,pila,instrucciones,file):
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

    def implements(self,ts,pila,instrucciones,file):
        try:
            vl = self.valor.get_Value(ts,pila)
            if isinstance(vl,simbolo):
                if vl.valor == '\\n':
                    print('>>\n')
                    file.write('\n')
                else:
                    if isinstance(vl.valor,str): vl.valor = vl.valor.replace('\\n','')
                    print(vl.valor)
                    file.write(''+str(vl.valor)+'')
            elif isinstance(vl,dict):
                if vl['valor'] == '\\n':
                    print('')
                    file.write('\n')
                else:
                    if isinstance(vl['valor'], str): vl['valor'] = vl['valor'].replace('\\n', '')
                    print(vl['valor'])
                    file.write(''+str(vl['valor'])+'')
        except:
            file.write("Error Inesperado, no se puede imprimir el valor, linea: "+str(self.linea)+'\n')

class salida(instruccion):

    def __init__(self,enum,linea):
        self.tipo_instruccion = enum
        self.linea = linea



