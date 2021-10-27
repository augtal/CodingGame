import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Inputs:
ABCs = [
" #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ",
"# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ",
"### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ",
"# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ",
"# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  "
] # the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.

l = 4 # the width L of a letter represented in ASCII art. All letters are the same width.
h = 5 # the height H of a letter represented in ASCII art. All letters are the same height.
t = "AB!!CD" # The line of text T, composed of N ASCII characters.

# Code
letters = []
for i in range(h):
    row = ABCs[i]
    amount = int(len(row) / l)
    characters = []
    for j in range(int(len(row) / l)):
        characters.append(row[j*l:j*l+l])
    letters.append(characters)

answer = [""] * h
t = t.upper()

for i in range(len(t)):
    letter = t[i]
    if letter.isalpha():
        letterACII = ord(letter) - 65 # A starts at 65, Z is 90
    else:
        letterACII = -1
    
    for j in range(h):
        answer[j] = answer[j] + letters[j][letterACII]
        

for i in range(h):
    print(answer[i])
