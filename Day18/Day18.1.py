#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 18: Lavaduct Lagoon ---

Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######

At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######

Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?

"""

grid = []
gridsize = 600
for y in range(gridsize):
    grid.append([])
    for x in range(gridsize):
        grid[-1].append(0)
y = x = 300
grid[y][x] = 1
out1 = 1

#with open('input--debug') as file:
with open('input') as file:
    for line in file:
        d,l = line.split()[:2]
        l = int(l)
        if d == 'U':
            for step in range(l):
                if grid[y-step-1][x] == 0:
                    grid[y-step-1][x] = 1
                    out1 += 1
            y -= l
        elif d == 'D':
            for step in range(l):
                if grid[y+step+1][x] == 0:
                    grid[y+step+1][x] = 1
                    out1 += 1
            y += l
        elif d == 'L':
            for step in range(l):
                if grid[y][x-step-1] == 0:
                    grid[y][x-step-1] = 1
                    out1 += 1
            x -= l
        else:
            for step in range(l):
                if grid[y][x+step+1] == 0:
                    grid[y][x+step+1] = 1
                    out1 += 1
            x += l
#print(out1)

for y in range(gridsize):
    if grid[y][0] == 0:
        grid[y][0] = 2
    if grid[y][-1] == 0:
        grid[y][-1] = 2
for x in range(gridsize):
    if grid[0][x] == 0:
        grid[0][x] = 2
    if grid[-1][x] == 0:
        grid[-1][x] = 2
change = True
while change:
    change = False
    for y in range(1,gridsize-1):
        for x in range(1,gridsize-1):
            if grid[y][x] == 0 and (grid[y-1][x] == 2 or grid[y][x-1] == 2):
                grid[y][x] = 2
                change = True
    for y in range(gridsize-2, 0, -1):
        for x in range(gridsize-2, 0, -1):
            if grid[y][x] == 0 and (grid[y+1][x] == 2 or grid[y][x+1] == 2):
                grid[y][x] = 2
                change = True

for y in range(1,gridsize-1):
    for x in range(1, gridsize-1):
        if not grid[y][x]: out1+=1

print(out1)

# 3701
# 41810 is too low. (I went into negatives a bit, and stuff did not blow up as I expected :/

# 3708
# 48652 is right. 
