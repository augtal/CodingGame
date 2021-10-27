import sys
import math

#The Goal
#Binary with 0 and 1 is good, but binary with only 0, or almost, is even better! Originally, this is a concept designed by Chuck Norris to send so called unary messages.
#Write a program that takes an incoming message as input and displays as output the message encoded using Chuck Norris’ method.

#Rules
#Here is the encoding principle:

#The input message consists of ASCII characters (7-bit)
#The encoded output message consists of blocks of 0
#A block is separated from another block by a space
#Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
#- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
#- Second block: the number of 0 in this block is the number of bits in the series

#Example
#Let’s take a simple example with a message which consists of only one character: Capital C. C in binary is represented as 1000011, so with Chuck Norris’ technique this gives:
#0 0 (the first series consists of only a single 1)
#00 0000 (the second series consists of four 0)
#0 00 (the third consists of two 1)
#So C is coded as: 0 0 00 0000 0 00

#Second example, we want to encode the message CC (i.e. the 14 bits 10000111000011) :
#0 0 (one single 1)
#00 0000 (four 0)
#0 000 (three 1)
#00 0000 (four 0)
#0 00 (two 1)
#So CC is coded as: 0 0 00 0000 0 000 00 0000 0 00

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Inputs
#00 0 0 0 00 00 0 0 00 0 0 0

message = "Chuck Norris' keyboard has 2 keys: white space and 0."
messageBinary = ""
for i in range(len(message)):
    messageBinary += bin(ord(message[i]))[2:] #turn message letter to ACII and then to binary ([2:] ignores the 0b added by python)

if len(messageBinary) < 7: #if message is shorter then 7 bits extend it to 7 bits
    messageBinary = "0"*(7-len(messageBinary)) + messageBinary

p = 0 #binary pointer
answer = ""
while p < len(messageBinary):
    if messageBinary[p] == '1':
        answer += "0 "
    else:
        answer += "00 "
    
    amount = 1
    p += 1
    
    if p < len(messageBinary):    
        while messageBinary[p-1] == messageBinary[p]:
            amount += 1
            p += 1
            
            if p >= len(messageBinary):
                break
    
    answer += "0"*amount + " "

print(answer[:-1])


