#payroll
name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
payRate = float(input("Enter hourly pay rate: "))
rate = int(input("Enter CPF contribution rate(%): "))
grossPay = hours * payRate
CPF = grossPay * rate / 100
netPay = grossPay - CPF


print("Payroll for ",name)
print("Number of hours worked in week: ",hours)
print('Hourly pay rate: ${0:.2f}'.format(payRate))
print('Gross pay = ${0:.2f}'.format(grossPay))
print('CPF contribution at ',rate,"% = ${0:.2f}".format(CPF))
print('Net pay = ${0:.2f}'.format(netPay))

