#!/bin/python

num  = input()
output = ""
formated = "  "

while num>0:
    output = str((num%2)) + output
    num = (num/2)

output = output[::-1]

while len(output)<32:
    output = output + "0"

output = output[::-1]

for x in range(32):
    formated = formated + output[x] + "  "

print(" ===============================================================================================")
print(" 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0")
print( formated )
print(" ===============================================================================================")
