#display certain pattern
n = int(input("enter n"))

for i in range (n,0,-1):
    print(((i-1)*2)*" ",end=" ")
    for j in range(n-i+1,0,-1):
        print(j,end=" ")
    print()


