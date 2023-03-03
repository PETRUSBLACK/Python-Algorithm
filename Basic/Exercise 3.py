# Write a program to accept a string from the user and display characters that 
# are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def Exercise_3():
    x = input("Enter a number ")
    for i in range(0, len(x), 2):
        print(x[i])

def Exercise_3b():
    x = input("Enter a number ")
    for i in x[0::2]:
        print(i)

Exercise_3b()

