# find days

def isLeap(a):
    if a % 4 ==0 and a % 100 != 0 or a % 400 ==0:
        return True
    else:# non leap
        return False

month = int(input("Enter month: "))
year = int(input("Enter year: "))
A= ["January","February","March","April","May","June","July","August","September","October","November","December"]

if 0<month<=12:
    if month == 2:
        if isLeap(year)== True:
            print(A[month-1],year,'has',29,'days')
        else:#non-leap
            print(A[month-1],year,'has',28,'days')
    elif month % 2== 0 and month <8 and month!=2:
        print(A[month-1],year,'has',30,'days')
    elif month % 2== 0 and month >=8:
        print(A[month-1],year,'has',31,'days')
    elif month % 2== 1 and month <9:
        print(A[month-1],year,'has',31,'days')
    elif month % 2== 1 and month >=9:
        print(A[month-1],year,'has',30,'days')
else:# invalid month
    print("Invalid month hohoho")
