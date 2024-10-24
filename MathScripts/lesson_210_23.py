#list

char = ['Mickey', 'Minnie', 'Bugs', 'Daffy']
sorted_char = sorted(char)
print(sorted_char)
print(char)
char.append('Spongebob') #list: Mickey, Minnie, Bugs, Daffy, Spongebob
# char.pop(1) #list: Mickey, Bugs, Daffy, Spongebob
# char.pop(1)
char.append('Spongebob')
char.append('Spongebob')
print(char)




# Tuple

# char1 = ('Mickey', 'Minnie', 'Bugs', 'Daffy')
# # char.append('Spongebob')
# char = ('Mickey', 'Minnie', 'Bugs', 'Daffy', 'Spongebob')
# print(char)

ages = [21, 34, 22, 56, 9]
print(max(ages))
print(min(ages))
print(sum(ages))
total_age = sum(ages)
length = len(ages)
print('Average age is ' + str(total_age / length))


#Set

char2 = {'Mickey', 'Minnie', 'Bugs', 'Daffy', 'Daffy', 'Minnie', 'Spongebob', 'Ferb', 'Goofy'}
char2.update(char1)
char.add('Donald')
print(char)


#Dictionary