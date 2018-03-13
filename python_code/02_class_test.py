#!/usr/bin/python
class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial(*{})".format(self.coeffs)

    def __add__(self, other):
        # Returns a new polynomial
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


# ___add__ is called a dunder method or data model method, the later can be googled to know how to declare it and use it
# To declare and initialize
p1 = Polynomial(1, 2, 3)  # x^2 + 2x + 3
p2 = Polynomial(6, 4, 5)  # 6x^2 + 4x + 5

print "{}\n{}".format(p1, p2)

# to add them
p3 = p1 + p2
print "{}".format(p3)

# to find out the degree of the polynomial
print "{}".format(len(p3))
