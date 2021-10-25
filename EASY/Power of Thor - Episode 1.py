import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

#Test Cases:
Positions = [31, 4, 31, 17]
Energy = 100

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = Positions

thorX = initial_tx
thorY = initial_ty

# game loop
while Energy > 0:
    remaining_turns = Energy  # The remaining amount of turns Thor can move. Do not remove this line.
    
    move = ""
    
    if thorY < light_y:
        move = move + "N"
        thorY = thorY + 1
    elif thorY > light_y:
        move = move + "S"
        thorY = thorY - 1
    
    if thorX > light_x:
        move = move + "W"
        thorX = thorX - 1
    elif thorX < light_x:
        move = move + "E"
        thorX = thorX + 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)
    
    Energy = Energy - 1
