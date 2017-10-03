class Figuras():

	def __init__(self):
		self.figura = None
		self.parametros = []

	def get_figura(self):
		return self.figura

	def set_figura(self, opcion):
		figuras = {1: 'Cuadrado', 2: "Rectangulo"}
		self.figura = figuras[opcion]

	def set_parametros(self, *args):
		self.parametros = args