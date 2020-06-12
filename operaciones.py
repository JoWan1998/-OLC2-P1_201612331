#CONSTRUCTORES PARA OPERACIONES, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA

from estructuras import *
from enumeradores import *
from TablaSimbolos import *

class operaciones:
    def descritpion(self):
        print("operaciones aritmeticas, logicas, relacionales para Augus")



class valor(operaciones):

    def __init__(self,valor,method,type):
        self.value = valor
        self.metodo = method
        self.tipo = type

    def get_tipo(self):
        return self.tipo

    def get_metodo(self):
        return self.metodo

    def get_Value(self,ts,pila):

        if isinstance(self.value,array_s) and self.metodo == METHOD_VALUE.ARREGLO:
            return self.value.implements(ts,pila)
        elif self.metodo == METHOD_VALUE.VARIABLE:
            value = ts.getSimbolo(self.value,pila)
            return value
        elif self.metodo == METHOD_VALUE.VALOR_UNICO:
            value = { 'valor': self.value, 'tipo': self.tipo,'method': 'valor'}
            return value
        elif self.metodo == METHOD_VALUE.APUNTADOR:
            value = ts.getSimbolo(self.value[1:],pila)
            value1 = {'valor': value.direccion, 'tipo': value.tipo, 'method': 'apuntador'}
            return value1
        elif self.metodo == METHOD_VALUE.READ:
            return None
        elif self.metodo == METHOD_VALUE.CONVERSION:
            value = self.value
            if isinstance(value,dict):
                if value['tipo'] == 'int' or value['tipo'] == 'float':
                    valor = value['value'].get_Value(ts,pila)
                    if isinstance(valor,dict):
                        if valor['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = {'valor': int(valor['valor']), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = {'valor': ord(str(valor['valor'])) ,'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor['tipo'] == TYPE_VALUE.APUNTADOR:
                            vl = ts.getPuntero(valor['valor'],pila)
                            if vl.tipo == TYPE_VALUE.NUMERIC:
                                value1 = {'valor': int(vl.valor), 'tipo': TYPE_VALUE.NUMERIC,'method': 'valor'}
                                return value1
                            elif vl.tipo == TYPE_VALUE.CHARACTER:
                                value1 = {'valor': ord(str(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return value1
                    elif isinstance(valor,simbolo):
                        if valor.tipo == TYPE_VALUE.NUMERIC:
                            value1 = {'valor': int(valor.valor), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor.tipo == TYPE_VALUE.CHARACTER:
                            value1 = {'valor': ord(str(valor.valor)) ,'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor.tipo == TYPE_VALUE.APUNTADOR:
                            vl = ts.getPuntero(valor.valor,pila)
                            if vl.tipo == TYPE_VALUE.NUMERIC:
                                value1 = {'valor': int(vl.valor), 'tipo': TYPE_VALUE.NUMERIC,'method': 'valor'}
                                return value1
                            elif vl.tipo == TYPE_VALUE.CHARACTER:
                                value1 = {'valor': ord(str(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return value1
                elif value['tipo'] == 'char':
                    valor = value['value'].get_Value(ts,pila)
                    if isinstance(valor,dict):
                        if valor['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = {'valor': chr(int(valor['valor'])), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = {'valor': (str(valor['valor'])) ,'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor['tipo'] == TYPE_VALUE.APUNTADOR:
                            vl = ts.getPuntero(valor['valor'],pila)
                            if vl.tipo == TYPE_VALUE.NUMERIC:
                                value1 = {'valor': chr(int(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC,'method': 'valor'}
                                return value1
                            elif vl.tipo == TYPE_VALUE.CHARACTER:
                                value1 = {'valor': (str(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return value1
                    elif isinstance(valor,simbolo):
                        if valor.tipo == TYPE_VALUE.NUMERIC:
                            value1 = {'valor': chr(int(valor.valor)), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor.tipo == TYPE_VALUE.CHARACTER:
                            value1 = {'valor': (str(valor.valor)) ,'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return value1
                        elif valor.tipo == TYPE_VALUE.APUNTADOR:
                            vl = ts.getPuntero(valor.valor,pila)
                            if vl.tipo == TYPE_VALUE.NUMERIC:
                                value1 = {'valor': chr(int(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC,'method': 'valor'}
                                return value1
                            elif vl.tipo == TYPE_VALUE.CHARACTER:
                                value1 = {'valor': (str(vl.valor)), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return value1


        else:
            print('Unexpected Error, the language can not identified the syntax')

        return None

class operacionesAritmeticas(operaciones):

    def __init__(self,tipo_operacion,valorizq,valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def get_Value(self,ts,pila):

        valoriz = None
        valorder = None

        if self.valorizq != None:
            valoriz = self.valorizq.get_Value(ts,pila)
        if self.valorder != None:
            valorder = self.valorder.get_Value(ts,pila)

        if self.operacion == OPERACION_ARITMETICA.SUMA:
            if isinstance(valoriz,simbolo):
                tipo = valoriz.tipo
                if isinstance(valorder,simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz.valor) + float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.CHARACTER:
                            valorin = str(valoriz.valor) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = str(valoriz.valor) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) + float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.CHARACTER:
                        if tipo1 == TYPE_VALUE.CHARACTER:
                            valorin = str(valoriz.valor) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = str(valoriz.valor) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = str(valoriz.valor) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = str(valoriz.valor) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin =  float(valiz.valor) + float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.CHARACTER:
                                valorin = str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz.valor) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) + float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif valiz.tipo == TYPE_VALUE.CHARACTER:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin =  str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.CHARACTER:
                                valorin = str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz.valor) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = str(valoriz.valor) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                    else:
                        return None
                elif isinstance(valorder,dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = float(valoriz.valor) + float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                valorin = str(valoriz.valor) + str(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            else:
                                return None
                        elif tipo == TYPE_VALUE.CHARACTER:

                                if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                    valorin = str(valoriz.valor) + str(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz.valor) + str(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                else:
                                    return None
            elif isinstance(valoriz,dict):
                tipo = valoriz['tipo']
                if isinstance(valorder,simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz['valor']) + float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.CHARACTER:
                            valorin = str(valoriz['valor']) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = str(valoriz['valor']) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) + float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.CHARACTER:
                        if tipo1 == TYPE_VALUE.CHARACTER:
                            valorin = str(valoriz['valor']) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = str(valoriz['valor']) + str(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = str(valoriz['valor']) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = str(valoriz['valor']) + str(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin =  float(valiz.valor) + float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.CHARACTER:
                                valorin = str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz['valor']) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) + float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif valiz.tipo == TYPE_VALUE.CHARACTER:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin =  str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.CHARACTER:
                                valorin = str(valiz.valor) + str(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz['valor']) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = str(valoriz['valor']) + str(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                    else:
                        return None
                elif isinstance(valorder,dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) + float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                valorin = str(valoriz['valor'])+str(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                return val
                            else:
                                return None
                        elif tipo == TYPE_VALUE.CHARACTER:
                                if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                    valorin = str(valoriz['valor']) + str(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                    valorin = str(valoriz['valor']) + str(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                                    return val
                                else:
                                    return None
        elif self.operacion == OPERACION_ARITMETICA.NEGATIVO:
            if valorder == None:
                if isinstance(valoriz, simbolo):
                    tipo = valoriz.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        valorin = -1 * (float(valoriz.valor))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            valorin = -1 * (float(valiz.valor))
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                elif isinstance(valoriz, dict):
                    tipo = valoriz['tipo']
                    if tipo == TYPE_VALUE.NUMERIC:
                        valorin = -1 * (float(valoriz['valor']))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            valorin = -1 * (float(valiz.valor))
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
        elif self.operacion == OPERACION_ARITMETICA.RESTA:
            if valorder == None:
                if isinstance(valoriz, simbolo):
                    tipo = valoriz.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        valorin = -1 * (float(valoriz.valor))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            valorin = -1 * (float(valiz.valor))
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                elif isinstance(valoriz, dict):
                    tipo = valoriz['tipo']
                    if tipo == TYPE_VALUE.NUMERIC:
                        valorin = -1 * (float(valoriz['valor']))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            valorin = -1 * (float(valiz.valor))
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
            else:
                if isinstance(valoriz, simbolo):
                    tipo = valoriz.tipo
                    if isinstance(valorder, simbolo):
                        tipo1 = valorder.tipo
                        if tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) - float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) - float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif tipo == TYPE_VALUE.APUNTADOR:
                            valiz = ts.getPuntero(valoriz.valor,pila)
                            if valiz.tipo == TYPE_VALUE.NUMERIC:
                                if tipo1 == TYPE_VALUE.NUMERIC:
                                    valorin = float(valiz.valor) - float(valorder.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif tipo1 == TYPE_VALUE.APUNTADOR:
                                    valer = ts.getPuntero(valorder.valor,pila)
                                    if valer.tipo == TYPE_VALUE.NUMERIC:
                                        valorin = float(valoriz.valor) - float(valer.valor)
                                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                        return val
                    elif isinstance(valorder, dict):
                        if valorder['method'] == 'valor':
                            if tipo == TYPE_VALUE.NUMERIC:
                                if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) - float(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                elif isinstance(valoriz, dict):
                    tipo = valoriz['tipo']
                    if isinstance(valorder, simbolo):
                        tipo1 = valorder.tipo
                        if tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) - float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) - float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif tipo == TYPE_VALUE.APUNTADOR:
                            valiz = ts.getPuntero(valoriz['valor'],pila)
                            if valiz.tipo == TYPE_VALUE.NUMERIC:
                                if tipo1 == TYPE_VALUE.NUMERIC:
                                    valorin = float(valiz.valor) - float(valorder.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif tipo1 == TYPE_VALUE.APUNTADOR:
                                    valer = ts.getPuntero(valorder.valor,pila)
                                    if valer.tipo == TYPE_VALUE.NUMERIC:
                                        valorin = float(valoriz['valor']) - float(valer.valor)
                                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                        return val

                        else:
                            return None
                    elif isinstance(valorder, dict):
                        if valorder['method'] == 'valor':
                            if tipo == TYPE_VALUE.NUMERIC:
                                if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) - float(valorder['valor'])
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val

                                else:
                                    return None
        elif self.operacion == OPERACION_ARITMETICA.MULTIPLICACION:
            if isinstance(valoriz, simbolo):
                tipo = valoriz.tipo
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz.valor) * float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) * float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) * float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) * float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) * float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz, dict):
                tipo = valoriz['tipo']
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz['valor']) * float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) * float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) * float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) * float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val

                    else:
                        return None
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) * float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val

                            else:
                                return None
        elif self.operacion == OPERACION_ARITMETICA.DIVISION:
            if isinstance(valoriz, simbolo):
                tipo = valoriz.tipo
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz.valor) / float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) / float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) / float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) / float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) / float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz, dict):
                tipo = valoriz['tipo']
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz['valor']) / float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) / float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) / float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) / float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val

                    else:
                        return None
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) / float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val

                            else:
                                return None
        elif self.operacion == OPERACION_ARITMETICA.RESIDUO:
            if isinstance(valoriz, simbolo):
                tipo = valoriz.tipo
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz.valor) % float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) % float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz.valor,pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) % float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz.valor) % float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz.valor) % float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz, dict):
                tipo = valoriz['tipo']
                if isinstance(valorder, simbolo):
                    tipo1 = valorder.tipo
                    if tipo == TYPE_VALUE.NUMERIC:
                        if tipo1 == TYPE_VALUE.NUMERIC:
                            valorin = float(valoriz['valor']) % float(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif tipo1 == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) % float(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif tipo == TYPE_VALUE.APUNTADOR:
                        valiz = ts.getPuntero(valoriz['valor'],pila)
                        if valiz.tipo == TYPE_VALUE.NUMERIC:
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                valorin = float(valiz.valor) % float(valorder.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif tipo1 == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = float(valoriz['valor']) % float(valer.valor)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val

                    else:
                        return None
                elif isinstance(valorder, dict):
                    if valorder['method'] == 'valor':
                        if tipo == TYPE_VALUE.NUMERIC:
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = float(valoriz['valor']) % float(valorder['valor'])
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val

                            else:
                                return None
        elif self.operacion == OPERACION_ARITMETICA.ABSOLUTO:
            if isinstance(valoriz, simbolo):
                tipo = valoriz.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    valorin = abs(float(valoriz.valor))
                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return val
                elif tipo == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        valorin = abs(float(valiz.valor))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
            elif isinstance(valoriz, dict):
                tipo = valoriz['tipo']
                if tipo == TYPE_VALUE.NUMERIC:
                    valorin = abs(float(valoriz['valor']))
                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return val
                elif tipo == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        valorin = abs(float(valiz.valor))
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val

        return None

class operacionesLogicas(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def get_Value(self, ts,pila):

        valoriz = None
        valorder = None


        if self.valorizq != None:
            valoriz = self.valorizq.get_Value(ts,pila)
        if self.valorder != None:
            valorder = self.valorder.get_Value(ts,pila)

        if self.operacion == OPERACION_LOGICA.NOT:
            if isinstance(valoriz,simbolo):
                tipo = valoriz.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz.valor
                    if numero == 0 or numero == 1:
                        valorin = 1 if(numero==0) else 0
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
            elif isinstance(valoriz,dict):
                tipo = valoriz['tipo']
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz['valor']
                    if numero == 0 or numero == 1:
                        valorin = 1 if(numero==0) else 0
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
        elif self.operacion == OPERACION_LOGICA.OR:
            if isinstance(valoriz,simbolo):
                tipo = valoriz.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz.valor
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  numero or numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero or numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                tipo = valoriz['tipo']
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz['valor']
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero or numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero or numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_LOGICA.AND:
            if isinstance(valoriz,simbolo):
                tipo = valoriz.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz.valor
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  numero and numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero and numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                tipo = valoriz['tipo']
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz['valor']
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero and numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin = numero and numero1
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_LOGICA.XOR:
            if isinstance(valoriz,simbolo):
                tipo = valoriz.tipo
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz.valor
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  (numero or numero1) and not (numero and numero1)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  (numero or numero1) and not (numero and numero1)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                tipo = valoriz['tipo']
                if tipo == TYPE_VALUE.NUMERIC:
                    numero = valoriz['valor']
                    if numero == 0 or numero == 1:
                        if isinstance(valorder, simbolo):
                            tipo1 = valorder.tipo
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder.valor
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  (numero or numero1) and not (numero and numero1)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            tipo1 = valorder['tipo']
                            if tipo1 == TYPE_VALUE.NUMERIC:
                                numero1 = valorder['valor']
                                if numero1 == 0 or numero1 == 1:
                                    valorin =  (numero or numero1) and not (numero and numero1)
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        return None

class operacionesRelacionales(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def get_Value(self,ts,pila):

        valoriz = None
        valorder = None

        if self.valorizq != None:
            valoriz = self.valorizq.get_Value(ts,pila)
        if self.valorder != None:
            valorder = self.valorder.get_Value(ts,pila)

        if self.operacion == OPERACION_RELACIONAL.MAYOR:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) > int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) > int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz.valor):
                                value += ord(n)
                            valorin = 1 if int(value) > int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            valorin = 1 if int(value1) > int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) > int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) > int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) > int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) > int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) > int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) > int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz['valor']):
                                value += ord(n)
                            valorin = 1 if int(value) > int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            valorin = 1 if int(value1) > int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) > int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) > int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) > int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) > int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) > int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) > int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) > int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) > int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) > int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_RELACIONAL.MAYOR_EQUALS:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) >= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) >= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz.valor):
                                value += ord(n)
                            valorin = 1 if int(value) >= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            valorin = 1 if int(value1) >= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) >= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) >= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) >= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) >= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) >= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) >= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz['valor']):
                                value += ord(n)
                            valorin = 1 if int(value) >= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            valorin = 1 if int(value1) >= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) >= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) >= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) >= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) >= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) >= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) >= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) >= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) >= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) >= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_RELACIONAL.MENOR:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) < int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) < int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz.valor):
                                value += ord(n)
                            valorin = 1 if int(value) < int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            valorin = 1 if int(value1) < int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) < int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) < int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) < int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) < int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) < int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) < int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) < int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) < int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) < int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) < int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) < int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) < int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) < int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz['valor']):
                                value += ord(n)
                            valorin = 1 if int(value) < int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            valorin = 1 if int(value1) < int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) < int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) < int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) < int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_RELACIONAL.MENOR_EQUALS:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) <= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) <= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz.valor) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz.valor):
                                value += ord(n)
                            valorin = 1 if int(value) <= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            valorin = 1 if int(value1) <= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz.valor):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder,simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value  = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder,dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value  = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder,simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value  = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder,dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value  = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) <= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) <= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(valoriz['valor']) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(valoriz['valor']) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            value = 0
                            for n in list(valoriz['valor']):
                                value += ord(n)
                            valorin = 1 if int(value) <= int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder.valor):
                                value += ord(n)
                            valorin = 1 if int(value1) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valoriz['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            valorin = 1 if int(value1) <= int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            value1 = 0
                            for n in list(valoriz['valor']):
                                value1 += ord(n)
                            value  = 0
                            for n in list(valorder['valor']):
                                value += ord(n)
                            valorin = 1 if int(value1) <= int(value) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) <= int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valer.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valoriz['valor']):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valer.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:

                                valorin = 1 if int(valiz.valor) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:

                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(valiz.valor) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:

                                    valorin = 1 if int(valiz.valor) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:

                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(valiz.valor) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                value = 0
                                for n in list(valiz.valor):
                                    value += ord(n)
                                valorin = 1 if int(value) <= int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder.valor):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value = 0
                                    for n in list(valiz.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                valorin = 1 if int(value1) <= int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                value1 = 0
                                for n in list(valiz.valor):
                                    value1 += ord(n)
                                value = 0
                                for n in list(valorder['valor']):
                                    value += ord(n)
                                valorin = 1 if int(value1) <= int(value) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    valorin = 1 if int(value1) <= int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                                elif valer.tipo == TYPE_VALUE.CHARACTER:
                                    value1 = 0
                                    for n in list(valiz.valor):
                                        value1 += ord(n)
                                    value = 0
                                    for n in list(valer.valor):
                                        value += ord(n)
                                    valorin = 1 if int(value1) <= int(value) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_RELACIONAL.EQUALS:
            if isinstance(valoriz, simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) == int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) == int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) == int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) == int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz.valor) == str(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz.valor) == str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz.valor) == str(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz.valor) == str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) == str(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) == str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) == str(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) == str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) == int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) == int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) == int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) == int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz, dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) == int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) == int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) == int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) == int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz['valor']) == str(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz['valor']) == str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz['valor']) == str(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz['valor']) == str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) == str(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) == str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) == str(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) == str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) == int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) == int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) == int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) == int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        elif self.operacion == OPERACION_RELACIONAL.NOTEQUALS:
            if isinstance(valoriz, simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) != int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) != int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz.valor) != int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz.valor) != int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz.valor) != str(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz.valor) != str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz.valor) != str(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz.valor) != str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) != str(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) != str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) != str(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) != str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) != int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) != int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) != int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) != int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
            elif isinstance(valoriz, dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) != int(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) != int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = 1 if int(valoriz['valor']) != int(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valoriz['valor']) != int(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.CHARACTER:
                    if isinstance(valorder, simbolo):
                        if valorder.tipo == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz['valor']) != str(valorder.valor) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz['valor']) != str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder, dict):
                        if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                            valorin = 1 if str(valoriz['valor']) != str(valorder['valor']) else 0
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valoriz['valor']) != str(valer.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if valiz.tipo == TYPE_VALUE.CHARACTER:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) != str(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) != str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.CHARACTER:
                                valorin = 1 if str(valiz.valor) != str(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.CHARACTER:
                                    valorin = 1 if str(valiz.valor) != str(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                    elif valiz.tipo == TYPE_VALUE.NUMERIC:
                        if isinstance(valorder, simbolo):
                            if valorder.tipo == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) != int(valorder.valor) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                                valer = ts.getPuntero(valorder.valor,pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) != int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
                        elif isinstance(valorder, dict):
                            if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                                valorin = 1 if int(valiz.valor) != int(valorder['valor']) else 0
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                            elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                                valer = ts.getPuntero(valorder['valor'],pila)
                                if valer.tipo == TYPE_VALUE.NUMERIC:
                                    valorin = 1 if int(valiz.valor) != int(valer.valor) else 0
                                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                    return val
        return None

class operacionesBit(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorde = valorde

    def get_Value(self,ts,pila):
        valoriz = None
        valorder = None

        if self.valorizq != None:
            valoriz = self.valorizq.get_Value(ts,pila)

        if self.valorde != None:
            valorder = self.valorde.get_Value(ts,pila)

        if self.operacion == OPERACION_BIT.ANDB:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) & int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) & int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) & int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) & int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) & int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) & int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) & int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) & int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) & int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
        elif self.operacion == OPERACION_BIT.ORB:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) | int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) | int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) | int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) | int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) | int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) | int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) | int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) | int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) | int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
        elif self.operacion == OPERACION_BIT.XORB:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) ^ int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) ^ int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) ^ int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) ^ int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) ^ int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) ^ int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) ^ int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) ^ int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) ^ int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
        elif self.operacion == OPERACION_BIT.SHIFTB:
            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) >> int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) >> int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) >> int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) >> int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) >> int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) >> int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) >> int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) >> int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) >> int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
        elif self.operacion == OPERACION_BIT.SHIFTA:

            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) << int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz.valor) << int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) << int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) << int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) << int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valoriz['valor']) << int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valoriz['valor']) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    if isinstance(valorder,simbolo):
                        if valorder.tipo == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) << int(valorder.valor)
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder.tipo == TYPE_VALUE.APUNTADOR or valorder.tipo == TYPE_VALUE.APUNTADORPILA:
                            valer = ts.getPuntero(valorder.valor,pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
                    elif isinstance(valorder,dict):
                        if valorder['tipo'] == TYPE_VALUE.NUMERIC:
                            valorin = int(valiz.valor) << int(valorder['valor'])
                            val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                            return val
                        elif valorder['tipo'] == TYPE_VALUE.APUNTADOR:
                            valer = ts.getPuntero(valorder['valor'],pila)
                            if valer.tipo == TYPE_VALUE.NUMERIC:
                                valorin = int(valiz.valor) << int(valer.valor)
                                val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                                return val
        elif self.operacion == OPERACION_BIT.NOTB:

            if isinstance(valoriz,simbolo):
                if valoriz.tipo == TYPE_VALUE.NUMERIC:
                    if isinstance(valorder,simbolo):
                        valorin = ~ int(valoriz.valor)
                        val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return val
                elif valoriz.tipo == TYPE_VALUE.APUNTADOR or  valoriz.tipo == TYPE_VALUE.APUNTADORPILA:
                    valiz = ts.getPuntero(valoriz.valor,pila)
                    valorin = ~ int(valiz.valor)
                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return val
            elif isinstance(valoriz,dict):
                if valoriz['tipo'] == TYPE_VALUE.NUMERIC:
                    valorin = ~ int(valoriz['valor'])
                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return val
                elif valoriz['tipo'] == TYPE_VALUE.APUNTADOR:
                    valiz = ts.getPuntero(valoriz['valor'],pila)
                    valorin = ~ int(valoriz['valor'])
                    val = {'valor': valorin, 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return val
        return None


