from ply import *
import gramatica
from instrucciones import *
from enumeradores import *
from operaciones import *
from array import *
from ascendente import *

file = open("./EJEMPLO_ENTRADA.txt")
data = file.read()

result = parse(data,0)
if result == None:
    print("errores")
print("finalizado")
