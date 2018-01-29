# find top 2

A=[]
B=[]
max=0
temp=''
max2=0
temp2=''
number= int(input("No of stuednts"))
for i in range(0,number):
    A.append(input("Name"))
    B.append(int(input("score")))


for i in range(0,number):
    if B[i] > max:
        max = B[i]
        temp = A[i]
    elif B[i]>max2 and B[i]<max:
        max2 = B[i]
        temp2 = A[i]

print('Highest score is',max,'from',temp,'\t','Second highest score is',max2,'from',temp2)
