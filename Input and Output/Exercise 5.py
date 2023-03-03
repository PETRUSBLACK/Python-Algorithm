# Accept a list of 5 float numbers as an input from the user

def Exercise_5():
    number = []
    count = 5
    for i in range(5):
        x = float(input("enter a float  "))
        number.append(x)
    print(number)

Exercise_5()