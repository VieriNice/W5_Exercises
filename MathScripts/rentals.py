import math

budget = 1000
van_cost = 250
tourist = 38 
van_tourist_cap = 15 
vans_needed = 3

print(str(vans_needed) + " are needed for 38 tourist.")


cost_of_rent = van_cost * vans_needed
print("$" + str(cost_of_rent) + " for 3 vans.")

cost_per_person = cost_of_rent // tourist
print("$" + str(cost_per_person) + " per person.")

money_leftover = budget - cost_of_rent

print("$" + str(money_leftover) + " is what's left of the budget.")