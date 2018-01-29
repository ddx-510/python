# convert format**
print("Kilograms Pounds")

for i in range(1,11):
    if int(i*2.2)>10 and i!=10:
        print("{0}{1:14.2f}".format(i,i*2.2))
    else:
        print("{0}{1:13.2f}".format(i,i*2.2))
