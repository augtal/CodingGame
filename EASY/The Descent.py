import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# Test Cases
# Descending mountains
inputs = [9,8,7,6,5,4,3,2]


height_list = []

# game loop
while True:
    for i in range(8):
        mountain_h = int(inputs[i])  # represents the height of one mountain.
        height_list.append(mountain_h)
    
    print(height_list)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print("4")
