import cmath

def quadratic_equation(a, b, c):
    """
        This method solves the quadratic given a, c, b from the form ax^2+bx+c=0.
        If the quadratic has multiple solutions, this will return them in a list.
        Since quadratics can have complex solutions, use cmath to compute the square root.
        If a divide by zero would occur, raise an appropriate exception.
        @:param a integer
        @:param b integer
        @:param c integer
    """
    # To make things easier, I've included the math already.
    positive_solution = (-b + cmath.sqrt(b ** 2 - (4 * a * c)))/(2 * a)
    negative_solution = (-b - cmath.sqrt(b ** 2 - (4 * a * c)))/(2 * a)

    return positive_solution, negative_solution
