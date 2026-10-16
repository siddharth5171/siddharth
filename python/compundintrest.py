principleamount = float(input("Enter the principal amount: "))
rateofinterest = float(input("Enter the rate of interest: "))
timeperiod = float(input("Enter the time period in months: "))
amount =principleamount
for i in range(int(timeperiod)):
    amount = amount + (amount * rateofinterest / 100)

print("The compound interest is:", amount - principleamount)
print("The total amount is:", amount)

