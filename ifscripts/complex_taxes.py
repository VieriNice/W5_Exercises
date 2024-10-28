import math 

gross_income = int(input('Welcome to tax center! Enter your grossincome: ')) 
marital_stat = str(input('Now that we know your gross income, let us know your marital status: '))


if gross_income < 12000:
    taxrate1 =  gross_income * .05
    print('Based on the gross income, you will be taxed: ' + str(taxrate1))
    print(marital_stat)
    weekly_tax1 = (gross_income * .05) / 52
    print('Your weekly tax is ' + str(weekly_tax1))
elif (12000 < gross_income < 24999):
    taxrate2 = gross_income * .06
    print('Based on the gross income, you will be taxed: ' + str(taxrate2))
    print(marital_stat)
    weekly_tax2 = (gross_income * .06) / 52
    print('Your weekly tax is ' + str(taxrate2)
elif (25000 <= gross_income >74999):
    taxrate3 = gross_income * .11
    print('Based on the gross income, you will be taxed: ' + str(taxrate3))
    print(marital_stat)
    weekly_tax3 = (gross_income * .11) / 52
    print('Your weekly tax is ' + str(weekly_tax3))
elif ( gross_income > 75000):
    taxrate4 = gross_income * .20
    print('Based on the gross income, you will be taxed: ' + str(taxrate4))
    print(marital_stat)
    weekly_tax4 = (gross_income * .20) / 52
    print('Your weekly tax is ' + str(weekly_tax4))







# else:
#     gross_pay = hours_worked * pay_rate
#     print('Based on the hours and rate given, your gross pay will be: ' + str(gross_pay)) 
    
