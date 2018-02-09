# reverse a number
def reverse_int(n):
    if len(n)==1:
        return n
    return n[-1]+reverse_int(n[:-1])

number = input("Enter a number: ")
print(reverse_int(number))
