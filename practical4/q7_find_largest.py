# find largest number in a list
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    if alist[0]>find_largest(alist[1:]):
        return alist[0]
    else:
        return find_largest(alist[1:])

# main
A= []
n= int(input("Enter no of numbers"))
for i in range(0,n):
    A.append(input("Number {0} is".format(i)))
print('LARGEST IS ',find_largest(A))
