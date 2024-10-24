import math

length = 20
width = 10

tiles_needed = length * width
extra_tiles = tiles_needed * .10

print(extra_tiles)

boxes = math.ceil(extra_tiles / 12)

print(boxes) #amount of boxes needed 



