# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is same after reverse. For example 545, 
# is the palindrome numbers

def Exercise_9(x):
    a = str(x)
    if a == a[::-1]:
        print("Yes", x, "is a palindrome number")
    else:
        print("No", x, "is not a palindrome number")

Exercise_9('loveee')
Exercise_9(565)