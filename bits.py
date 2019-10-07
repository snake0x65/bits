#!/bin/python

MAX = 0xffffffff
output = ""
formated = "  "

num  = input("val->  ")
val = num
# check for MAX
if num > MAX:
    print("No more then 32 bits, please.")
    exit(-1)
# convert to binary form
while num>0:
    output = str((num%2)) + output
    num = (num/2)
# reverse
output = output[::-1]
# add missing bits
while len(output)<32:
    output = output + "0"
#reverse back
output = output[::-1]
# format
for x in range(32):
    formated = formated + output[x] + "  "

# print
print(" DEC: {:d}, HEX: {:x}, OCT: {:o}, BIN: {:b}".format(val, val, val, val))
print(" ===============================================================================================")
print(" 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0")
print( formated )
print(" ===============================================================================================")
