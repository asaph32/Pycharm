import unittest
import dominio
from dominio import Biblioteca,Livro,Funcionario,Usuario,Emprestimo

class TestCase(unittest.TestCase):
    def test_verificarLivroJaEmprestado(self):
       livro1 = Livro(2,"bananas feias")
       usuario = Usuario("Asaph")
       func = Funcionario("08912546","Irvayne")
       biblioteca = dominio.Biblioteca()
       biblioteca.cadastrarLivro(livro1)
       biblioteca.cadastrarFuncionario(func)
       biblioteca.realizarEmprestimo(func,livro1,usuario)
       self.assertEqual(livro1,"livro ja emprestado")

    def test_buscarLivroNaoCadastradoNaBiblioteca(self):
       biblioteca = dominio.Biblioteca()
       livro1 = Livro(2, "Fiz Xixi na Cama")
       func = Funcionario("08912710311","Asaph")
       biblioteca.cadastrarFuncionario(func)
       self.assertEqual(livro1,"Livro nao cadastrado")

    def test_devolverumlivronaoemprestado(self):
       biblioteca = dominio.Biblioteca()
       func = Funcionario("000000","Irvayne")
       livro1 = Livro(3,"Biblia")
       biblioteca.cadastrarFuncionario(func)
       biblioteca.cadastrarLivro(livro1)
       biblioteca.realizarDevolucao(func,livro1)
       self.assertEqual(livro1,"Livro nao foi emprestado!!")

    def test_limitarEmprestimoDeNoMaximo3Livros(self):

        func = Funcionario("08912710311","Irvayne")
        usuario = Usuario("asaph")

        livro = Livro(1, "bebe recem nascido")
        livro1 = Livro(2, "O maior mentiroso do mundo")
        livro2 = Livro(3, "FrontEnd para Iniciantes")
        livro3 = Livro(4, "de A a Z")

        biblioteca = dominio.Biblioteca()
        biblioteca.cadastrarLivro(livro)
        biblioteca.cadastrarLivro(livro1)
        biblioteca.cadastrarLivro(livro2)
        biblioteca.cadastrarLivro(livro3)

        biblioteca.realizarEmprestimo(func,livro,usuario)
        biblioteca.realizarEmprestimo(func, livro1, usuario)
        biblioteca.realizarEmprestimo(func, livro2, usuario)
        biblioteca.realizarEmprestimo(func, livro3, usuario)

        self.assertEqual(livro3,"Voce atingiu o limite maximo de emprestimos")

    def test_solicitarEmprestimoComFuncionarioInvalido(self):
       biblioteca = dominio.Biblioteca()
       func1 = Funcionario("159753","Tiririca")
       usuario = Usuario("Asaph")
       livro = Livro(5,"Vinho Novo é o Melhor")
       biblioteca.cadastrarLivro(livro)
       biblioteca.realizarEmprestimo(func1,livro,usuario)
       self.assertEqual(func1,"Funcionario Invalido!!")

    def test_realizandoMaisTestes(self):
        biblioteca = dominio.Biblioteca()
        func = Funcionario("08912710311","asaph")
        book1 = Livro(1,"Culinarias 2022")
        usuario = Usuario("Asaph")
        biblioteca.cadastrarLivro(book1)
        biblioteca.cadastrarFuncionario(func)
        biblioteca.realizarEmprestimo(func,book1,usuario)
        self.assertEqual(book1,book1,print("Emprestimo Realizado com sucesso"))

    def test_outroTeste(self):
        biblioteca = dominio.Biblioteca()
        book = Livro(3,"Xurastey")
        usuario = Usuario("Asaph")
        func = Funcionario("159753258","Matheus")
        biblioteca.cadastrarLivro(book)
        biblioteca.cadastrarFuncionario(func)
        biblioteca.realizarEmprestimo(func,book,usuario)
        biblioteca.realizarDevolucao(func,book)
        self.assertEqual(book,book,print("Devoluçao Realizada com sucesso"))









