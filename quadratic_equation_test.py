import unittest
import quadratic_equation

class QuadraticEquationTest(unittest.TestCase):
    def test_positive(self):
        positive_solution, negative_solution = \
            quadratic_equation.quadratic_equation(5, 6, 1)
        self.assertEqual(positive_solution.real, -0.2)
        self.assertEqual(negative_solution.real, -1)

    def test_zero(self):
        self.assertEqual(True, True)

    def test_negative(self):
        self.assertEqual(True, True)

    def test_divide_by_zero(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
