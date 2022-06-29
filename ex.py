import unittest

class MyTeste(unittest.TestCase):
    def test_soma(self):
        soma = 10 + 10
        self.assertEqual(soma,8)

    def test_subtracao(self):
        subtracao = 20 - 10
        self.assertEqual(subtracao,10)

    def test_divisao(self):
        divisao = 10 / 2
        self.assertEqual(divisao,3)

    def test_multiplicacao(self):
        multiplicacao = 2 * 2
        self.assertEqual(multiplicacao,4)

    def test_CalcularAreaDoQuadrado(self, b = 3 , h = 5):
        CalcularQuadrado = b * h
        self.assertEqual(CalcularQuadrado,10)

    def test_CalcularTriangulo(self, b = 2 , h = 3):
        CalcularTriangulo = (b * h) / 2
        self.assertEqual(CalcularTriangulo,3)

    def test_ApenasTentandoAlgoDiferente(self):
        nome = str(input("Informe o seu nome : "))
        peso = float(input("Informe seu peso : "))
        altura = float(input("Informe a sua altura : "))
        imc = peso / (altura * altura)
        self.assertEqual(imc,26.122448979591837)

    def test_Bhaskara(self):
        b = float(input("Informe o B :"))
        a = float(input("Informe o A : "))
        c = float(input("Informe o C : "))
        delta = (b*b) - 4 * a * c
        self.assertEqual(delta,-8)

    def test_calcularVertice(self):
        b = float(input("Informe o valor de B : "))
        a = float(input("Informe o valor de A : "))
        delta = float(input("Informe o valor de Delta : "))
        xvertice = - b / (2 * a)
        yvertice = delta / (4 * a)
        self.assertEqual(xvertice,-4)
        self.assertEqual(yvertice,8)



