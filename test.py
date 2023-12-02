import unittest
from calc import Calc

class TestCalculator(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calc()
  
  def test_addition(self):
    self.assertEqual(self.calculator.addition(4,7), 11)
  
  def test_subtraction(self):
    self.assertEqual(self.calculator.subtraction(10,5), 5)
  
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)
  
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)

if __name__ == "__main__":
  unittest.main()