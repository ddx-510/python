# factorize by prime number

import math

A = []

def fact(a):
    i = 2
    flag = True # isPrime
    while i <= int(math.sqrt(a)) + 1:
        if a % i == 0:
            A.append(i)
            flag = False
            fact(int(a / i))
            i += 1
            break
        i += 1
    if flag: # a is now a prime
        A.append(a)


fact(int(input("Number is: ")))
print(A)
