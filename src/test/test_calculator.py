import unittest
from app.calculator import Calculator
a=4
b=2
somme=a+b
sommeKo=a+b+1
c=1.2
d=2.2
e="un"
f="deux"
class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(a+a,b)
        self.assertEqual(somme+a, result)
        
    def test_calculator_add_method_returns_correct_result2(self):
        result = self.calc.add(a,b)
        self.assertEqual(somme, result,"{!r} + {!r} ne font pas {!r}".format(a,b,result))    
        
    def test_calculator_add_method_returns_false(self):
        result = self.calc.add(a,b)
        self.assertNotEquals(sommeKo, result,"ca ne doit pas etre pareil")
            
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, e, f)
    
    def test_calculator_returns_error_message_if_first_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, e, a)
        
    def test_calculator_returns_error_message_if_second_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, b, f)       
if __name__ == '__main__':
    unittest.main()