# find the greatest common divider
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print('the greatest common divider is',gcd(int(input("No 1 is ")),int(input("No 2 is "))))
