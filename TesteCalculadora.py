from Calculadora import *
import unittest

class MyTeste(unittest.TestCase):

    def test_somaDeDoisNumerosPositivos(self):
        c = Calculadora(1,2)
        c.soma(1,2)
        resulatdo_obtido = c.testSomaNumerosPositivos(1,2)
        self.assertEqual(True,resulatdo_obtido)

    def test_somaDeDoisNumerosNegativos(self):
        c = Calculadora(-1,-2)
        c.soma(-1,-2)
        resultado_obtido = c.testSomaNumerosNegativos(-1,-2)
        self.assertEqual(True,resultado_obtido)

    def test_subtracaoNumerosPositivos(self):
        c = Calculadora(2,2)
        resultado_obtido = c.testSubtracaoNumerosPositivos(2,2)
        self.assertEqual("deu certo",resultado_obtido)

    def test_subtracaoNumerosNegativos(self):
        c = Calculadora(-2,-2)
        resultado_obtido = c.testSubtracaoNumerosNegativos(-2,-2)
        self.assertEqual("deu foi certo",resultado_obtido)

    def test_multiplicacaoNumerosPositivos(self):
        c = Calculadora(3,3)
        resultado_obtido = c.testMultiplicacaoNumerosPositivos(3,3)
        self.assertEqual("Verdade",resultado_obtido)

    def test_multiplicacaoNumerosNegativos(self):
        c = Calculadora(-3,-3)
        resultado_obtido = c.testeMultiplicacaoNumerosNegativos(-3,-3)
        self.assertEqual("Verdade",resultado_obtido)

    def test_DivisaoNumerosPositivos(self):
        c = Calculadora(2,2)
        resultado_obtido = c.testeDivisaoNumerosPositivos(2,2)
        self.assertEqual(True,resultado_obtido)

    def test_DivisaoPorZero(self):
        c = Calculadora(2,0)
        resultado_obtido = c.testeDivisaoNumerosPositivos(2,0)
        self.assertEqual(False,resultado_obtido)

