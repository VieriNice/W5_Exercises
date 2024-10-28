department_code = int(input('Welcome to fresh farms! Please insert the department code you want to reach: '))

if department_code == 1:
    print('Welcome to marketing!')
elif department_code == 5 :
    print('You have reached Human Resources!.')
elif department_code == 10: 
    print('You have reached accounting!')
elif department_code == 12:
    print('Welcome to the legal department!')
elif department_code == 18:
    print('You reached the IT department!')
elif department_code == 20:
    print('You have reached customer relations!')
else: 
    print('Uh oh, code doesn\'t match any of our record')