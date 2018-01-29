# display table
print("Miles Kilometers Kilometers Miles")
for i in range(1,11):
    if 7<=i<=9:
        print("{0}{1:11.3f}{2:7}{3:15.3f}".format(i,i*1.609,i*5+15,(i*5+15)/1.609))
    elif i==10:
        print("{0}{1:10.3f}{2:7}{3:15.3f}".format(i,i*1.609,i*5+15,(i*5+15)/1.609))
    else:
        print("{0}{1:10.3f}{2:8}{3:15.3f}".format(i,i*1.609,i*5+15,(i*5+15)/1.609))
