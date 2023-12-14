#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 14: Parabolic Reflector Dish ---

You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....

You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1

The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?

Your puzzle answer was 107430.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....

After 2 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O

After 3 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O

This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?

"""
from copy import deepcopy as cp

rounds = 1000000000
oldpf = []
pf = []
l = 0
with open('input') as file:
    for line in file:
        pf.append([])
        for col in line.rstrip():
            pf[l].append(col)
        l += 1

nr = len(pf)
nc = len(pf[0])
boulder_col = []
boulder_row = []
l_boulder_col = []
l_boulder_row = []
for x in range(nc):
    boulder_col.append([-1])
for y in range(nr):
    boulder_row.append([-1])
    for x in range(nc):
        if pf[y][x] == '#':
            boulder_col[x].append(y)
            boulder_row[y].append(x)
    boulder_row[y].append(nr)
for x in range(nc):
    boulder_col[x].append(nc)
for i in range(nc):
    while boulder_col[i][-2] + 1 == boulder_col[i][-1]:
        boulder_col[i].pop()
    while boulder_col[i][0] + 1 == boulder_col[i][1]:
        boulder_col[i].pop(0)
for i in range(nr):
    while boulder_row[i][-2] + 1 == boulder_row[i][-1]:
        boulder_row[i].pop()
    while boulder_row[i][0] + 1 == boulder_row[i][1]:
        boulder_row[i].pop(0)
for i in range(nr):
    l_boulder_row.append(len(boulder_row[i]))
for i in range(nc):
    l_boulder_col.append(len(boulder_col[i]))
print(boulder_col)
print(boulder_row)
rounds = 100
for r in range(rounds):
    if not r % 1000000: print(r)

    for col in range(nc):
        n = 1
        s = boulder_col[col][0]
        while n < l_boulder_col[col]:
            e = boulder_col[col][n]
            c = s+1
            b = 0
            while c < e:
                if pf[c][col] == '.':
                    s = c
                    while c < e-1:
                        c += 1
                        if pf[c][col] == 'O':
                            b += 1
                            pf[c][col] = '.'
                    for i in range(b):
                        pf[s+i][col] = 'O'
                c += 1
            n += 1
            s = e
    """
    print()
    for row in range(len(pf)):
        p = ''
        for col in pf[row]:
            p += col
        print(p)
    """
    for row in range(nr):
        n = 1
        s = boulder_row[row][0]
        while n < l_boulder_row[row]:
            e = boulder_row[row][n]
            c = s+1
            b = 0
            while c < e:
                if pf[row][c] == '.':
                    s = c
                    while c < e-1:
                        c += 1
                        if pf[row][c] == 'O':
                            b += 1
                            pf[row][c] = '.'
                    for i in range(b):
                        pf[row][s+i] = 'O'
                c += 1
            n += 1
            s = e
    """
    print()
    for row in range(len(pf)):
        p = ''
        for col in pf[row]:
            p += col
        print(p)
    """
    for col in range(nc):
        n = l_boulder_col[col] - 1
        s = boulder_col[col][-1]
        while n >= 0:
            n -= 1
            e = boulder_col[col][n]
            c = s-1
            b = 0
            while c > e:
                if pf[c][col] == '.':
                    s = c
                    while c > e+1:
                        c -= 1
                        if pf[c][col] == 'O':
                            b += 1
                            pf[c][col] = '.'
                    for i in range(b):
                        pf[s-i][col] = 'O'
                c -= 1
            s = e
    """
    print()
    for row in range(len(pf)):
        p = ''
        for col in pf[row]:
            p += col
        print(p)
    """
    for row in range(nr):
        n = l_boulder_row[row] - 1
        s = boulder_row[row][-1]
        while n >= 0:
            n -= 1
            e = boulder_row[row][n]
            c = s-1
            b = 0
            while c > e:
                if pf[row][c] == '.':
                    s = c
                    while c > e+1:
                        c -= 1
                        if pf[row][c] == 'O':
                            b += 1
                            pf[row][c] = '.'
                    for i in range(b):
                        pf[row][s-i] = 'O'
                c -= 1
            s = e
    """
    print()
    for row in range(len(pf)):
        p = ''
        for col in pf[row]:
            p += col
        print(p)
    """
    o = 0
    for row in range(nr):
        for col in pf[row]:
            if col == 'O':
                o += nr-row
    print(r,o)
    #if o == '64':
    #    print('Right weight @round:', r)
    #if oldpf == pf:
    #    print('No more change.')
    #    break
    #oldpf = cp(pf)

out1 = 0
for row in range(nr):
    for col in pf[row]:
        if col == 'O':
            out1 += nr-row
print(out1)

# pt1:
# 107430

# rounds repeat with a period of 7 , after three steps. for test input.
# rounds repeat with period 9, after 93 steps. 
# answer should be 96317
"""
print()
for row in range(len(pf)):
    p = ''
    for col in pf[row]:
        p += col
    print(p)
"""
