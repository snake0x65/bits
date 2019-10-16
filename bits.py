#!/usr/bin/python
#
#   Copyright 2019 Vitaly Rodionov
#   Author: Vitaly Rodionov <vitaly.rodionov@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#

import sys
import getopt

argv = sys.argv[1:]
num = 0
base = 10
MAX = 0xffffffff
output = ""
formated = "  "

try:
    # define the getopt parameters
    opts, args = getopt.getopt(argv, 'b:o:x:d:', ['bin', 'oct', 'hex', 'dec'])
    # check parameters
    if len(opts) == 0 or len(opts) > 1:
      print ('usage: bits.py -{b,o,x,d} <value>')
    else:
      # iterate the options and get the corresponding values
      for opt, arg in opts:
        if opt == '-b':
            base = 2
        elif opt == '-o':
            base = 8
        elif opt == '-x':
            base = 16
        elif opt == '-d':
            base = 10
except getopt.GetoptError:
    print ('usage: bits.py -{b,o,x,d} <value>')
    sys.exit(2)

num = int(str(arg),base)
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
# reverse back
output = output[::-1]
# format
for x in range(32):
    formated = formated + output[x] + "  "
# ..and print
print(" ===============================================================================================")
print(" DEC: {:d}, HEX: {:x}, OCT: {:o}, BIN: {:b}".format(val, val, val, val))
print(" ===============================================================================================")
print(" 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0")
print( formated )
print(" ===============================================================================================")
