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

Your puzzle answer was 540131.

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 86879020.
"""

def check(y,x,l):
    has_symbol = False
    rangestart = x - (l+1) # *123.
    rangeend = x+1 # exclusive
    if rangestart == -1:
        rangestart = 0
    else:
        if es[y][rangestart] != '.':
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


def givenumrev(y,x):
    g = ''
    while es[y][x].isdigit():
        g = es[y][x] + g
        x += -1
        if x < 0: break
    return g

def givenum(y,x):
    g = ''
    while es[y][x].isdigit():
        g += es[y][x]
        x += 1
    return g

def checkline(y, x):
    r = []
    last = False
    g = givenumrev(y,x-1)
    h = givenum(y,x)
    g += h
    if g: r.append(g)
    if not h:
        g = givenum(y,x+1)
        if g: r.append(g)
    return r


def is_gear(y, x):
    ratio = []
    pn = givenumrev(y,x-1)
    if pn: ratio.append(pn)
    pn = givenum(y,x+1)
    if pn: ratio.append(pn)
    if y > 0: ratio += checkline(y-1, x)
    if y < my: ratio += checkline(y+1, x)
    print(ratio)
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

