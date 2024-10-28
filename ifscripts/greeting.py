
time_inserted = int(input('Enter the time you are starting your shift: '))

if ( time_inserted > 5 and time_inserted <= 10 ): 
    print("Good Morning")
elif 10 <= time_inserted < 17: 
    print('Good Day!')
elif 23 >= time_inserted >= 4:
    print("what are you doing up so late")
else: 
    print('Good evening')
    
    