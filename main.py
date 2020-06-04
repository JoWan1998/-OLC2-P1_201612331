from ply import *
import gramatica
from instrucciones import *
from enumeradores import *
from operaciones import *
from estructuras import *
from ascendente import *
from ply import errores

file = open("./EJEMPLO_ENTRADA.txt")
data = file.read()
errores = errores.errores()

result = parse(data,1,errores)
if result == None:
    print("errores")
print("finalizado")
