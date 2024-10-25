# Boolean operators

# recycling inputs
cans = 0
bottles = 0
boxes = 0


print(cans < bottles and bottles < 5) # 'and' both conditions have to be true 
print(cans < bottles or bottles < 5) # 'or' either condtiion must be true

if (cans >0 or bottles > 0) or not boxes > 0:
    print('Call the recycling service for pickup')
elif boxes != 0:
    print("We've gotta do something with these boxes")






## Match Case

greeting = input('Enter your greeting: ')

match greeting: 
    case 'Hello': 
        print('Hello to you too!')
    case 'Good morning!':
        print('Good morning to you too!')
    case other:
        print('Oh, you don\'t say')

if greeting == 'Hello':
    print('Hello to you')
elif greeting == 'Good morning':
    print('Good morning')
else: 
    print('Oh, you don\'t say?')