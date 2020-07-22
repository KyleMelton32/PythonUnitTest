import unittest
import quadratic_equation


class QuadraticEquationTest(unittest.TestCase):
    def test_positive(self):
        """ This tests when the discriminate is positive. (b^2 - 4 * a * c) > 0 """
        positive_solution, negative_solution = \
            quadratic_equation.quadratic_equation(5, 6, 1)
        self.assertEqual(positive_solution.real, -0.2)
        self.assertEqual(negative_solution.real, -1)

    @unittest.skip("Test not developed")
    def test_zero(self):
        """ This tests when the discriminate is zero. (b^2 - 4 * a * c) = 0 """
        pass

    @unittest.skip("Test not developed")
    def test_negative(self):
        """ This tests when the discriminate is negative. (b^2 - 4 * a * c) < 0 """
        pass

    def test_divide_by_zero(self):
        """ This tests when the a divide by zero would occur (a=0) """
        with self.assertRaises(ZeroDivisionError):
            positive_solution, negative_solution = \
                quadratic_equation.quadratic_equation(0, 6, 1)


if __name__ == '__main__':
    unittest.main()
