import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2, 2)
		self.assertEquals(self.calc.obtener_resultado(), 4)

	def test_restar_2_menos_2_igual_0(self):
		self.calc.resta(2, 2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def tearDown(self):
		pass

if __name__ == '__main__': # pragma: no cover
	unittest.main()
