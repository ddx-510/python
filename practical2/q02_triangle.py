# triangle valid perimeter
perimeter = 0

s1 = int(input("Enter side 1:"))
s2 = int(input("Enter side 2:"))
s3 = int(input("Enter side 3:"))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    perimeter += s1+s2+s3
    print("perimeter = ",perimeter)
else:# invalid
    print("Invalid triangle!")
