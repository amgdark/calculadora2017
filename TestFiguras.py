import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):
	
	def test_menu_cuadrado(self):
		figuras = Figuras()
		figuras.set_figura(1)

		self.assertEquals(figuras.get_figura(), "Cuadrado")	

	def test_menu_rectangulo(self):
		figuras = Figuras()
		figuras.set_figura(2)

		self.assertEquals(figuras.get_figura(), "Rectangulo")	

	def test_area_rectangulo_lado1_4_lado2_6(self):
		figuras = Figuras()
		figuras.set_figura(1)
		figuras.set_parametros(4, 6)
		self.assertEquals(figuras.resultado(), 24)	


if __name__ == '__main__':
	unittest.main()