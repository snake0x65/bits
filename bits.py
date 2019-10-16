#!/usr/bin/python
import sys
import getopt

MAX = 0xffffffff
output = ""
formated = "  "
argv = sys.argv[1:]
num = 0

try:
    # Define the getopt parameters
    opts, args = getopt.getopt(argv, 'b:o:x:d', ['bin', 'oct', 'hex', 'dec'])
    # Check if the options' length is 2 (can be enhanced)
    if len(opts) == 0 and len(opts) > 1:
      print ('usage: add.py -a <first_operand> -b <second_operand>')
    else:
      # Iterate the options and get the corresponding values
      for opt, arg in opts:
        if opt == '-b':
            num = int(str(arg),2)
        elif opt == '-o':
            num = int(str(arg),8)
        elif opt == '-x':
            num = int(str(arg),16)
        elif opt == '-d':
            num = int(str(arg),10)

except getopt.GetoptError:
    # Print something useful
    print ('usage: add.py -a <first_operand> -b <second_operand>')
    sys.exit(2)

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
