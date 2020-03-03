from MathOperations.addition import Addition
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.multiplication import Multiplication
from MathOperations.subtraction import Subtraction
from MathOperations.root import Root


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b)

    def Fraction(self, a, b):
        self.Result = Division.fraction(a, b)

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)

    def Root(self, a, b):
        self.Result = Root.root(a, b)

    def Logarithm(self, a, b):
        self.Result = Log.logarithm(a, b)

    '''
    def multiplication(self, a, b):
        return a * b

    def squared(self, a):
        return a * a 

    def squareRoot(self, a):
        import math
        return (math.sqrt(a))
    '''

