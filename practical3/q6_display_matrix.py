# print a random matirx
import random
def print_matrix(n):
    for i in range (0,n):
        for j in range(0,n):
            print(random.randint(0,1),end=' ')
        print()

n = int(input("Enter number"))
print_matrix(n)
