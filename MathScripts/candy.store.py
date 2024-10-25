
candy1 = ('Apple Gum', 'Cherry Dust', 'Strawberry Chews')
candy2 = ('Blueberry Blast', 'Green Apple Gum', 'Pear Drops')



new_candy = set()
new_candy.add((candy1[2], candy2[0])) #Strawberry Chews and Blueberry Blast 
new_candy.add((candy1[0], candy2[1])) #Apple Gum and Green Apple Gum

print("Today's candy options include: " + str(new_candy))


