class Calculadora:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def testSomaNumerosPositivos(self,valor1,valor2):
        if (valor1 >= 0 and valor2 >= 0):
            return True
        else:
            return False

    def testSomaNumerosNegativos(self,valor1,valor2):
        if (valor1 < 0 and valor2 < 0):
            return True
        else:
            return False

    def testSubtracaoNumerosPositivos(self,valor1,valor2):
        if(valor1 >= 0 and valor2 >= 0):
            return "deu certo"
        else:
            return "deu errado"

    def testSubtracaoNumerosNegativos(self,valor1,valor2):
        if (valor1 < 0 and valor2 < 0):
            return "deu foi certo"
        else:
            return "deu foi é errado"

    def testMultiplicacaoNumerosPositivos(self,valor1,valor2):
        if (valor1 >= 0 and valor2 >= 0):
            return "Verdade"
        else:
            return "Falso"

    def testeMultiplicacaoNumerosNegativos(self,valor1,valor2):
        if (valor1 < 0 and valor2 < 0):
            return "Verdade"
        else:
            return "Falso"

    def testeDivisaoNumerosPositivos(self,valor1,valor2):
        if (valor2 != 0 and (valor1/valor2 >= 0 or valor1/valor2 <= 0 )):
            return True
        else:
            return False


    def soma(self,valor1,valor2):
        soma = valor1 + valor2

    def subtracao(self,valor1,valor2):
        subtracao = valor1 - valor2

    def multiplicacao(self,valor1,valor2):
        multiplicacao = valor1 * valor2

    def divisao(self,valor1,valor2):
        divisao = valor1 / valor2
