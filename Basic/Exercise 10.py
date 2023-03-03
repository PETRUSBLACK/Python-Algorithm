# Given a two list of numbers, write a program to create a new list such that the new 
# list should contain odd numbers from the first list and even numbers from the 
# second list.

def Exercise_10(y,x):
    a = []
    # for i in x[::2]:
    #     a.append(i)
    for i in range(len(y)):
        if i % 2 != 0:
            a.append(y[i])
    for i in range(len(x)):
        if i % 2 == 0:
            a.append(x[i])
    print(a)

        
Exercise_10('love','love')
