import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Test Cases
N = 6
Inp = [4, -2, 2, -8, 4, 5]

n = N  # the number of temperatures to analyse
temps = []

for t in Inp:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    temps.append(t)

if len(temps) >= 1:
    minValue = 5526
    tempIndex = -1

    for i in range(len(temps)):
        value = temps[i]
        if value < 0:
            value = value * -1
        
        if value < minValue:
            minValue = value
            tempIndex = i
        elif minValue == value:
            if temps[tempIndex] < temps[i]:
                tempIndex = i

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(temps[tempIndex])
else:
    print(0)