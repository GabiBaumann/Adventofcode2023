#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 86879020.
"""

def check(y,x,l):
    has_symbol = False
    rangestart = x - (l+1) # *123.
    rangeend = x+1 # exclusive
    if rangestart == -1:
        rangestart = 0
    else:
        if es[y][rangestart] != '.': # can make this redundant by specialcasing number after symbol 
            has_symbol = True
    if not has_symbol and y > 0:
        # check above
        for i in range(rangestart,rangeend):
            if es[y-1][i] not in no_symbol:
                has_symbol = True
    if not has_symbol and y < my:
        # check below
        for i in range(rangestart,rangeend):
            if es[y+1][i] not in no_symbol:
                has_symbol = True
    if has_symbol:
        return True
    return False


def is_gear(y,x):
    ratio = []
    if es[y][x-1].isdigit():
        pn = es[y][x-1]
        for i in range(x-2, -1, -1):
            if es[y][i].isdigit():
                pn = es[y][i] + pn
            else: break
        ratio.append(pn)
    if es[y][x+1].isdigit():
        pn = es[y][x+1]
        for i in range(x+2, mx):
            if es[y][i].isdigit():
                pn += es[y][i]
            else: break
        ratio.append(pn)
    if y > 0:
        last = False
        if es[y-1][x-1].isdigit():
            pn = es[y-1][x-1]
            for i in range(x-2, -1, -1):
                if es[y-1][i].isdigit():
                    pn = es[y-1][i] + pn
                else: break
            for i in range(x, mx):
                if es[y-1][i].isdigit():
                    pn += es[y-1][i]
                    last = True
                else: break
            ratio.append(pn)
        elif es[y-1][x].isdigit():
            last = True
            pn = es[y-1][x]
            for i in range(x+1, mx):
                if es[y-1][i].isdigit():
                    pn += es[y-1][i]
                else: break
            ratio.append(pn)
        if not last and es[y-1][x+1].isdigit():
            pn = es[y-1][x+1]
            for i in range(x+2, mx):
                if es[y-1][i].isdigit():
                    pn += es[y-1][i]
                else: break
            ratio.append(pn)
    if y < my:
        last = False
        if es[y+1][x-1].isdigit():
            pn = es[y+1][x-1]
            for i in range(x-2, -1, -1):
                if es[y+1][i].isdigit():
                    pn = es[y+1][i] + pn
                else: break
            for i in range(x, mx):
                if es[y+1][i].isdigit():
                    pn += es[y+1][i]
                    last = True
                else: break
            ratio.append(pn)
        elif es[y+1][x].isdigit():
            last = True
            pn = es[y+1][x]
            for i in range(x+1, mx):
                if es[y+1][i].isdigit():
                    pn += es[y+1][i]
                else: break
            ratio.append(pn)
        if not last and es[y+1][x+1].isdigit():
            pn = es[y+1][x+1]
            for i in range(x+2, mx):
                if es[y+1][i].isdigit():
                    pn += es[y+1][i]
                else: break
            ratio.append(pn)
    if len(ratio) == 2:
        return int(ratio[0]) * int(ratio[1])
    return 0

    
no_symbol = '0123456789.\n'
es = []
with open('input') as file:
#with open('input--debug') as file:
    for line in file:
        es.append(line)

mx = len(line) - 1
my = len(es) - 1

ypos = result = 0
for line in es:
    in_num = False
    xpos = 0
    for char in line:
        if char.isdigit():
            if not in_num:
                pn = char
                in_num = True
            else:
                pn += char
        elif char == '.' or char == '\n':
            if in_num:
                in_num = False
                if check(ypos,xpos,len(pn)):
                    result += int(pn)
        else: #(Symbol)
            if in_num:
                in_num = False
                result += int(pn)

        xpos += 1
    ypos += 1


ypos = result2 = 0
for line in es:
    xpos = 0
    for char in line:
        if char == '*':
            result2 += is_gear(ypos,xpos)
        xpos += 1
    ypos += 1

print(result, result2)

# part1:
# 541515 is too high. (was completely untested firt successful run :)
# 539458 is too low. 
# 540131 fixed line end case. Right.

# part2:
# 86879020

