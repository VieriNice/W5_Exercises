#Pet Store calculator



#Current cats to be fed 
num_cats = int(input("How many cats need to be fed today?"))

cat_food = {
     'fromm': int(input("How much fromm do we have?")),
     'purina': int(input('How much purina do we have?')),
     'kirkland': int(input('How much kirland cat food in inventory?'))}

cat_serving = 0.10
cats_fed = num_cats * cat_serving

# Confirming current number of cats and available food
print(f'Number of cats: {num_cats}')
print(f'Cat food in stock: {cat_food}')


print(f'Number of cats: {num_cats}')
print(f'Cat food in stock: {cat_food}')



#Calculate the unknown

if cat_food['kirkland'] > 0: 
    cat_food['kirkland'] = cat_food['kirkland'] - (cats_fed)
elif cat_food['fromm'] > 0:
        cat_food['fromm'] = cat_food['fromm'] - (cats_fed)

else: 
    cat_food['purina'] = cat_food['purina'] - (cats_fed)



print(f'Number of cats: {num_cats}')
print(f'Cat food in stock: {cat_food}')

print(f'After feeding the cats: {cat_food}')