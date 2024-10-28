

pay_rate = int(input('Welcome to workforce! Enter the pay you desire: ')) 
hours_worked = int(input('Now that we know how much you want to get paid, let\'s see how many hours you want to work: '))


if hours_worked > 40:
    overtime = pay_rate * hours_worked * 1.5
    print('Based on the hours and pay rate given, your pay gross pay with overtime will be: ' + str(overtime))
else:
    gross_pay = hours_worked * pay_rate
    print('Based on the hours and rate given, your gross pay will be: ' + str(gross_pay)) 
    