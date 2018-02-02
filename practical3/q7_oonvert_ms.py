#convert ms to s
def convert_ms(n):
    h = ((n//1000)//3600)
    temp = n-h*3600*1000
    min1 = (temp//1000)//60
    temp2 = temp - min1*60*1000
    s = (temp2//1000)

    return str(h)+":"+str(min1)+":"+str(s)

n = int(input("enter a number"))
print(convert_ms(n))
