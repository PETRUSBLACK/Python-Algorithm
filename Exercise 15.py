# Exercise 15: Write a function called exponent(base, exp) that returns an int 
# value of base raises to the power of exp.

def Exercise_16(base, exp):
    b = exp - 1
    c = range(base)
    for i in range(b):
        s = c[-1] + 1
        base *= s
    print(base)

Exercise_16(2, 5)

