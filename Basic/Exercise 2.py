# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

def exercise_2():
    a = 0;
    for i in range(10):
        c = a + i
        print("Current number is",i, "This is the previous number", c-i,"This is the sum", c)
        a = i

exercise_2()