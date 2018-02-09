# summation of digits
def sum_digits(n):
    if len(n)==1:
        return int(n)
    return sum_digits(n[1:])+int(n[0])

# main
number = input("Enter a number: ")
print(sum_digits(number))
