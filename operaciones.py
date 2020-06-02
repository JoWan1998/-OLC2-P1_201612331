#



class operaciones:
    def descritpion(self):
        print("operaciones aritmeticas, logicas, relacionales para Augus")


class operacionesAritmeticas(operaciones):

    def __init__(self,tipo_operacion,valorizq,valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("aritmeticas")


class operacionesLogicas(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Logicas")


class operacionesRelacionales(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Relacionales")


class operacionesBit(operaciones):

    def __init__(self, tipo_operacion, valorizq, valorde):
        self.operacion = tipo_operacion
        self.valorizq = valorizq
        self.valorder = valorde

    def implements(self):
        print("Bit a Bit")

