__author__ = 'lucas.glimfjord'

def halve(value):
    result = value / 2.0
    return result

def add(term1, term2):
    result = term1 + term2
    return result

def subtract(term1, term2):
    result = term1 - term2
    return result

def multiply(factor1, factor2):
    result = factor2*factor1
    return result

def square(value):
    result = value**2
    return result

def square_of_square_root(value):
    result = (value**1/2)**2
    return result

absolutevalue = square_of_square_root

print(absolutevalue(-4))