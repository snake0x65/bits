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
tmp = 0
base = 10
MAX = 0xffffffff
output = ""
formated = "  "
sbits = list()
cbits = list()

def Usage():
    print ('Usage: bits.py -{b,o,x,d,i} <value> -{s,c) <bit,bit,bit,...>')
    print ('Example: bits.py -x FF00FF00 -s 0,1,2 -c 31,24,6')
    print ('         bits.py -d 200 -s 0,1,2,17 -c 31,24,6')
    print ('         bits.py -b 10100001110  -s 0,1,2 -c 31,24,6')
    sys.exit(-1)

def Error():
    print("Error in params")
    sys.exit(-3)

try:
    opts, args = getopt.getopt(argv, 'b:o:x:d:s:c:', ['bin', 'oct', 'hex', 'dec', 'set', 'clear'])
    if len(opts) == 0 or len(opts) > 3:
        Usage()
    else:
        for opt, arg in opts:
            if opt == '-b':
                base = 2
                tmp = arg
            elif opt == '-o':
                base = 8
                tmp = arg
            elif opt == '-x':
                base = 16
                tmp = arg
            elif opt == '-d':
                base = 10
                tmp = arg
            elif opt == '-h':
                Usage()

    num = int(str(tmp),base)
    print
    for opt, arg in opts:
        if opt == '-s':
            sbits = list(arg.split(","))
            print(" Set bits {}".format(sbits))
            for b in sbits:
                if int(b) > 31:
                    Error()
                num = num | (1 << int(b))
        elif opt == '-c':
            cbits = list(arg.split(","))
            print(" Clr bits {}".format(cbits))
            for b in cbits:
                if int(b) > 31:
                    Error()
                num = num & ~(1 << int(b))

    val = num

    if num > MAX:
        print("No more then 32 bits, please.")
        exit(-1)

    while num > 0:
        output = str((num%2)) + output
        num = (num/2)

    output = output[::-1]

    while len(output)<32:
        output = output + "0"

    output = output[::-1]

    for x in range(32):
        formated = formated + output[x] + "  "

    print(" ===============================================================================================")
    print(" DEC: {:d}, HEX: {:x}, OCT: {:o}, BIN: {:b}".format(val, val, val, val))
    print(" ===============================================================================================")
    print(" 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0")
    print( formated )
    print(" ===============================================================================================")
    print

except getopt.GetoptError:
    Usage()
