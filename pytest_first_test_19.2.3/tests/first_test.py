import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_substraction_calculate_correctly(self):
        assert self.calc.substraction(self, 6, 2) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 6, 2) == 8
        
        
