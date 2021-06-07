"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiply(self):
        assert 6 == calculator.multiply(2, 3)

    def test_divide(self):
        assert 12 == calculator.divide(144, 12)

    def test_add_neg():
        assert 3 == calculator.add(12, -9)
    
    def test_subtract_neg():
        assert 21 == calculator.subtract(12, -9)
    
    def test_multiply_neg():
        assert -21 == calculator.multiply(-3,7)

    def test_divide_neg():
        assert -5 == calculator.divide(-70, 14)