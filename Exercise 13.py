# Print multiplication table form 1 to 10

def Exercise_13():
    # a = [1,2,3,4,5,6,7,8,9,10]
    # b = [1,2,3,4,5,6,7,8,9,10]
    # c = 0
    # d = []
    # for i in a:
    #     for v in b:
    #         print(i*v)

    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=None)
        print("\t\t")

Exercise_13()