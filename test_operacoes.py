'''
Todo o codigo foi feito pelo Vinicius Gabriel 📚
Você pode ver mais dos meus codigo no github: https://github.com/Vinibiiel?tab=repositories
Precisando de um programador python? https://www.linkedin.com/in/vinibiiel-01/

Todos podem utilizar desse codigo, seja em trabalhos ou projetos (●'◡'●), não há nada de autoral
'''
import unittest # import the module for the tests
from operacoes import Operacoes # Import the class who has the operations
op = Operacoes() # Instance the class

# We need to put a module method, in the argument in the class
class TesteOperacoes(unittest.TestCase):
    # Test for the function sum

    # Let's use "assertEqual" to check if the return was the desired one, and I used other unittest methods, to test other things
    def test_defSum(self):
        self.assertEqual(op.sum(5,10),15,msg=f'Erro na soma, não foi retornado o valor {15}')
        self.assertIsInstance(op.sum(5,10),int,"Não retornou o tipo INT")

    # Test for the function subtraction
    def test_defSubtraction(self):
        self.assertEqual(op.subtraction(5,10),-5,'Erro na Subtração')
        self.assertIsNotNone(op.subtraction(5,10),msg='Retornado um valor Nulo na função subtraction')

    # Test for the function Multiply
    def test_defMultiply(self):
        self.assertEqual(op.multiply(5,10),50,'Erro na Multiplicação')
        self.assertNotEqual(op.multiply(5,10), 10, msg='Multiplicação errada')

    # Test for the function divide and divideRest
    def test_defDivide(self):
        self.assertEqual(op.divide(10,5),2,'Erro na Divisão')

        entrys1 = list(range(2,22,2))
        for entrada in entrys1:
            with self.subTest(entrada=entrada):
                self.assertEqual(op.divideRest(entrada,2),
                0,
                msg='Resto diferente de 0'
                )
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # Tee argument verbosity, we used for the module, return us the complete test string, if you want a test string more shortened, use verbosity=1 or verbosity=0

