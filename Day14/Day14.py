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

Your puzzle answer was 96317.
"""

from copy import deepcopy as cp

rounds = 1000000000
l_log = 12 # max period! 
out1 = out2 = cycle = period = 0
boulder_col = []
boulder_row = []
l_boulder_col = []
l_boulder_row = []
pf = []
pf_log = []
for i in range(l_log):
    pf_log.append([])

#with open('input--debug') as file:
with open('input') as file:
    for line in file:
        pf.append([])
        for col in line.rstrip(): pf[-1].append(col)

nr = len(pf)
nc = len(pf[0])
for x in range(nc): boulder_col.append([-1])
for y in range(nr):
    boulder_row.append([-1])
    for x in range(nc):
        if pf[y][x] == '#':
            boulder_col[x].append(y)
            boulder_row[y].append(x)
    boulder_row[y].append(nr)
for x in range(nc): boulder_col[x].append(nc)
for i in range(nc):
    while boulder_col[i][-2] + 1 == boulder_col[i][-1]: boulder_col[i].pop()
    while boulder_col[i][0] + 1 == boulder_col[i][1]: boulder_col[i].pop(0)
for i in range(nr):
    while boulder_row[i][-2] + 1 == boulder_row[i][-1]: boulder_row[i].pop()
    while boulder_row[i][0] + 1 == boulder_row[i][1]: boulder_row[i].pop(0)
for i in range(nr): l_boulder_row.append(len(boulder_row[i]))
for i in range(nc): l_boulder_col.append(len(boulder_col[i]))

while pf not in pf_log:
    pf_log[cycle%l_log] = cp(pf)

    for col in range(nc):
        n_field = 1
        start = boulder_col[col][0]
        while n_field < l_boulder_col[col]:
            end = boulder_col[col][n_field]
            count = start + 1
            boulders = 0
            while count < end:
                if pf[count][col] == '.':
                    start = count
                    while count < end - 1:
                        count += 1
                        if pf[count][col] == 'O':
                            boulders += 1
                            pf[count][col] = '.'
                    for i in range(boulders):
                        pf[start+i][col] = 'O'
                count += 1
            n_field += 1
            start = end
    if not cycle: # count for pt.1
        for row in range(nr):
            for col in pf[row]:
                if col == 'O': out1 += nr-row

    for row in range(nr):
        n_field = 1
        start = boulder_row[row][0]
        while n_field < l_boulder_row[row]:
            end = boulder_row[row][n_field]
            count = start+1
            boulders = 0
            while count < end:
                if pf[row][count] == '.':
                    start = count
                    while count < end - 1:
                        count += 1
                        if pf[row][count] == 'O':
                            boulders += 1
                            pf[row][count] = '.'
                    for i in range(boulders):
                        pf[row][start+i] = 'O'
                count += 1
            n_field += 1
            start = end
    
    for col in range(nc):
        n_field = l_boulder_col[col] - 1
        start = boulder_col[col][-1]
        while n_field >= 0:
            n_field -= 1
            end = boulder_col[col][n_field]
            count = start-1
            boulders = 0
            while count > end:
                if pf[count][col] == '.':
                    start = count
                    while count > end + 1:
                        count -= 1
                        if pf[count][col] == 'O':
                            boulders += 1
                            pf[count][col] = '.'
                    for i in range(boulders):
                        pf[start-i][col] = 'O'
                count -= 1
            start = end
    
    for row in range(nr):
        n_field = l_boulder_row[row] - 1
        start = boulder_row[row][-1]
        while n_field >= 0:
            n_field -= 1
            e = boulder_row[row][n_field]
            count = start-1
            boulders = 0
            while count > end:
                if pf[row][count] == '.':
                    start = count
                    while count > end + 1:
                        count -= 1
                        if pf[row][count] == 'O':
                            boulders += 1
                            pf[row][count] = '.'
                    for i in range(boulders):
                        pf[row][start-i] = 'O'
                count -= 1
            start = e
    cycle += 1

# found the period
h = cycle
while pf != pf_log[h%l_log]:
    period += 1
    h -= 1
offset = (cycle // period * period + rounds) % period
#print('@cycle:', cycle, 'Period:', period, 'Offset:', offset)
for row in range(nr):
    for col in pf_log[offset][row]:
        if col == 'O': out2 += nr-row

print(out1, out2)
# 107430 96344

# rounds repeat with a period of 7 , after three steps. for test input.
# rounds repeat with period 9, after 93 steps. for my input.
# answer should be 96317. it is. 
