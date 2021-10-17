from app.calculator import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 5, 5) == 25

   def test_division_calculate_correctly(self):
       assert self.calc.division(self, 4, 2) == 2

   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(self, 10, 2) == 8

   def test_subtraction_adding_correctly(self):
       assert self.calc.adding(self, 15, 3) == 18
