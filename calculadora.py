# coding: utf-8
# implementado CI con travis

class Calculadora():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        self.resultado = num1 + num2

    def resta(self, num1, num2):
        print (u"ejemplo de línea sin ejecución")
        self.resultado = num1 - num2

    def prueba(self):
        if True and False or True and False:
            pass
        if False:
            pass
        for x in xrange(1, 10):
            pass

        try:
            pass
        except Exception as e:
            raise e
