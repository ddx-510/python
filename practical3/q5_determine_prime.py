# is prime for 4000 primes
import math
s=0
k=0
i=0

def isPrime(number):
    flag =  False
    for i in range(1,int(math.sqrt(number))+1):
        if number % i == 0 and i!=1 and number!=i:
            flag = True
            break
    if flag == False and number !=1 :
        return True
    else:
        return False

while s<4000:
    i+=1
    if isPrime(i) == True:
        print(i,end="\t")
        k+=1
        s+=1
    if k == 10:
        print()
        k=0

