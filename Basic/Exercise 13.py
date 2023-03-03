# Print multiplication table form 1 to 10

def Exercise_13():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="|")
        print("\t\t")

Exercise_13()