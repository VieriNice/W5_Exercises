# Define the known 

pumpkins = int(input("How many pumpkins do you have? (Whole numbers only)")) #optimal pumpkin inventory = 1500

p_ship = 400

# Calculate the unknown
if pumpkins < 600:   
    pumpkins = pumpkins + (2 * p_ship)
    print("Pumpkins Ordered")
    print("Pumpkin Emergency! Only " + str(pumpkins) + " pumpkins")
elif pumpkins < 1200:
    pumpkins += p_ship # means pumpkins = pumpkins + P_ship
    print("Time to order some pumpkin. ( " + str(pumpkins) + ")  left")
elif pumpkins == 1500:
    print("Whoa! ")

else: 
    print("No order needed")

# Display the results
# print("Now we have " + str(pumpkins) + " pumpkins")

apples = int(input("How many apples are in inventory?"))

if apples < 0:
    print("There is an error in inventory. PLease review.")
elif apples != 0:
    print("Yea, we got apples.")
else:
    print("we are out of apples")