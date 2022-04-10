import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    """
       TestCalculator checks if all functions of the Calculator are working properly.
    """

    # Testing print memory function
    def test_print_memory(self) -> None:
        self.calculator = Calculator()
        self.memory = self.calculator.return_memory
        print(self.memory)

    # Testing addition function
    def test_add(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.add(2) == 2

    # Testing subtraction function
    def test_subtract(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.subtract(2) == -2

    # Testing multiplication function
    def test_multiply(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.multiply(5) == 0

    # Testing division function
    def test_divide(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.divide(5) == 0

    # Testing nth root function
    def test_n_root(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.n_root(5) == 0

    # Testing memory reset function
    def test_reset(self) -> None:
        self.calculator = Calculator()
        assert self.calculator.memory_reset() == None


if __name__ == '__main__':
    unittest.main()
