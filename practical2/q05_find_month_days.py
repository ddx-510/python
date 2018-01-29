# find days

def isLeap(a):
    if a % 4 ==0 and a % 100 != 0 or a % 400 ==0:
        return True
    else:# non leap
        return False

month = int(input("Enter month: "))
year = int(input("Enter year: "))

if 0<month<=12:
    if month == 2:
        if isLeap(year)== True:
            print('NO OF DAYS IS',28)
        else:#non-leap
            print('NO OF DAYS IS',29)
    elif month % 2== 0 and month <8 and month!=2:
        print('NO OF DAYS IS',30)
    elif month % 2== 0 and month >=8:
        print('NO OF DAYS IS',31)
    elif month % 2== 1 and month <9:
        print('NO OF DAYS IS',31)
    elif month % 2== 1 and month >=9:
        print('NO OF DAYS IS',30)
else:# invalid month
    print("Invalid month hohoho")

