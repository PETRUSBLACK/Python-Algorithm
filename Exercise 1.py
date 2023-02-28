# Given two integer numbers return their product only if the product is equal 
# to or lower than 1000, else return their sum.

def Exercise_1(x, y):
    if x * y <= 1000:
        print(x * y)
    else:
        print(x + y)

Exercise_1(20, 30)
Exercise_1(40, 30)
