# sum series
def m(a):
    sum = 0
    for i in range(0,a):
        sum += i/(i+1)
    return sum
def output(a):
    print("i\t\tm(i)")
    for i in range(0,a):
        print("{0}\t\t{1:.4f}".format(i,m(i)))

n = int(input("Enter the number"))
output(n)
