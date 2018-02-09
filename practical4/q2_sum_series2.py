# 1/3 + 2/5 +...+ i/(2i+1)
def sumseries2(a):
    if a == 1:
        return 1/3
    else:
        return sumseries2(a-1) + a/(2*a+1)

# main
n = int(input("Enter number n"))
print("{0:.2f}".format(sumseries2(n)))
