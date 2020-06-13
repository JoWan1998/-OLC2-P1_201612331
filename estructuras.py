#CLASE CONSTRUCTORA DE EJECUCIONES DE ARRAY, AUGUS
#JOSE WANNAN @2020
#UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
from enumeradores import *
from TablaSimbolos import *

class array_s:
    def __init__(self, enum,valor=list,variable=None,posicion=None):
        self.value = valor
        self.method = enum
        self.variable = variable
        self.posicion = posicion

    def implements(self,ts,pila):
        if self.method == ARRAY_METHOD.GET:
            posicion = self.posicion
            variable = ts.getSimbolo(self.variable,pila)
            if variable.tipo == TYPE_VALUE.ARREGLO:
                try:
                    return self.insertInArray(ts,variable.valor,posicion,pila)
                except:
                    return None
            elif variable.tipo == TYPE_VALUE.CHARACTER:
                try:
                    pos = self.posicion[0].get_Value(ts,pila)
                    lis = list(variable.valor)
                    m = ''
                    if isinstance(pos,simbolo):
                        m = lis[int(pos.valor)]
                    elif isinstance(pos,dict):
                        m = lis[int(pos['valor'])]

                    return {'valor': m, 'method': 'valor', 'tipo': TYPE_VALUE.CHARACTER}
                except:
                    return None
            else:
                return None
        elif self.method == ARRAY_METHOD.INSTANCIA:
            return {'valor':{},'method':'arreglo','tipo': TYPE_VALUE.ARREGLO}
        else:
            return None

    def setList(self,ts,dictt,pila,pos,cont):
        cont -= 1
        el = next(pos)
        vl = el.get_Value(ts, pila)
        if cont ==0:
            if isinstance(vl,simbolo):
                if isinstance(vl.valor,int) or isinstance(vl.valor,float): vl.valor = int(vl.valor)
                mm = dictt[vl.valor]
                if isinstance(mm, dict):
                    value1 = {'valor': mm, 'tipo': TYPE_VALUE.ARREGLO, 'method': 'valor'}
                    return value1
                elif isinstance(mm, str):
                    value1 = {'valor': str(mm), 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                    return value1
                elif isinstance(mm, int):
                    value1 = {'valor': int(mm), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return value1
            elif isinstance(vl,dict):
                if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                mm = dictt[vl['valor']]
                if isinstance(mm,dict):
                    value1 = {'valor': mm, 'tipo': TYPE_VALUE.ARREGLO, 'method': 'valor'}
                    return value1
                elif isinstance(mm,str):
                    value1 = {'valor': str(mm), 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                    return value1
                elif isinstance(mm,int):
                    value1 = {'valor': int(mm), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                    return value1
        else:
            if isinstance(vl, simbolo):
                if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                return self.setList(ts,dictt[vl.valor],pila,pos,cont)
            elif isinstance(vl, dict):
                if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                return self.setList(ts,dictt[vl['valor']],pila,pos,cont)

    def insertInArray(self,ts,lists,pos,pila):
        try:
            con = len(pos)
            con -=1
            posi = iter(pos)
            mm = next(posi)
            vl = mm.get_Value(ts, pila)
            if con > 0:
                if isinstance(vl, simbolo):
                    if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                    return (self.setList(ts,lists[vl.valor],pila,posi,con))
                elif isinstance(vl, dict):
                    if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                    return (self.setList(ts, lists[vl['valor']], pila, posi, con))
            else:

                if isinstance(vl, simbolo):
                    if isinstance(vl.valor, int) or isinstance(vl.valor, float): vl.valor = int(vl.valor)
                    mm = lists[vl.valor]
                    if isinstance(mm, dict):

                        value1 = {'valor': mm, 'tipo': TYPE_VALUE.ARREGLO, 'method': 'valor'}
                        return value1
                    elif isinstance(mm, str):
                        value1 = {'valor': str(mm), 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                        return value1
                    elif isinstance(mm, int):
                        value1 = {'valor': int(mm), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return value1

                elif isinstance(vl, dict):
                    if isinstance(vl['valor'], int) or isinstance(vl['valor'], float): vl['valor'] = int(vl['valor'])
                    mm = lists[vl['valor']]
                    if isinstance(mm, dict):
                        value1 = {'valor': mm, 'tipo': TYPE_VALUE.ARREGLO, 'method': 'valor'}
                        return value1
                    elif isinstance(mm, str):
                        value1 = {'valor': str(mm), 'tipo': TYPE_VALUE.CHARACTER, 'method': 'valor'}
                        return value1
                    elif isinstance(mm, int):
                        value1 = {'valor': int(mm), 'tipo': TYPE_VALUE.NUMERIC, 'method': 'valor'}
                        return value1
        except:
            return None

    def new_array(self):
        print('setting new array')

    def  getting_array(self):
        print('getting array')
        return None

    def setting_array(self):
        print('setting array')


