# 1+ 1/2 + 1/3 + 1/4....+ 1/i
def sumseries1(a):
    if a == 1:
        return 1
    else:
        return sumseries1(a-1) + 1/a

# main
n = int(input("Enter number n"))
print("{0:.2f}".format(sumseries1(n)))
