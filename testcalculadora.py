import exemplo
import unittest


class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
       testeSoma = exemplo.calculadora()
       testeSoma.valor1 = 2
       testeSoma.valor2 = 3
       soma = testeSoma.valor1 + testeSoma.valor2
       self.assertEqual(soma,5)

    def test_subtracao(self):
        testeSubtracao = exemplo.calculadora()
        testeSubtracao.valor1 = 4
        testeSubtracao.valor2 = 2
        subtracao = testeSubtracao.valor1 - testeSubtracao.valor2
        self.assertEqual(subtracao,2)

    def test_multiplicacao(self):
        testMultiplicacao = exemplo.calculadora()
        testMultiplicacao.valor1 = 2
        testMultiplicacao.valor2 = 3
        multiplicacao = testMultiplicacao.valor1 * testMultiplicacao.valor2
        self.assertEqual(multiplicacao,6)

    def test_divisao(self):
        testDivisao = exemplo.calculadora()
        testDivisao.valor1 = 10
        testDivisao.valor2 = 2
        divisao = testDivisao.valor1 / testDivisao.valor2
        self.assertEqual(divisao,5)

    def test_calcularIMC(self):
        calculoIMC = exemplo.CalculoImc()
        calculoIMC.peso = 4
        calculoIMC.altura = 2
        realizarCalculoIMC = calculoIMC.peso / (calculoIMC.altura * calculoIMC.altura)
        self.assertEqual(realizarCalculoIMC,1.0)

    def test_numerosIguais(self):
        self.assertEqual(4,4)

    def test_numerosDiferentes(self):
        self.assertEqual(5,6)

    def test_testandoOutrosTestes(self):
        self.assertEqual(5 + 5,4 + 6)

    def test_Essediferente(self):
        self.assertEqual(10 / 2,4 + 1)


    print("Testes concluidos com sucesso!!")






