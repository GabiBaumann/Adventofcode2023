#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 23: A Long Walk ---

The Elves resume water filtering operations! Clean water starts flowing over the edge of Island Island.

They offer to help you go over the edge of Island Island, too! Just hold on tight to one end of this impossibly long rope and they'll lower you down a safe distance from the massive waterfall you just created.

As you finally reach Snow Island, you see that the water isn't really reaching the ground: it's being absorbed by the air itself. It looks like you'll finally have a little downtime while the moisture builds up to snow-producing levels. Snow Island is pretty scenic, even without any snow; why not take a walk?

There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), and steep slopes (^, >, v, and <).

For example:

#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#

You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. Because of all the mist from the waterfall, the slopes are probably quite icy; if you step onto a slope tile, your next step must be downhill (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, never step onto the same tile twice. What is the longest hike you can take?

In the example above, the longest hike you can take is marked with O, and your starting position is marked S:

#S#####################
#OOOOOOO#########...###
#######O#########.#.###
###OOOOO#OOO>.###.#.###
###O#####O#O#.###.#.###
###OOOOO#O#O#.....#...#
###v###O#O#O#########.#
###...#O#O#OOOOOOO#...#
#####.#O#O#######O#.###
#.....#O#O#OOOOOOO#...#
#.#####O#O#O#########v#
#.#...#OOO#OOO###OOOOO#
#.#.#v#######O###O###O#
#...#.>.#...>OOO#O###O#
#####v#.#.###v#O#O###O#
#.....#...#...#O#O#OOO#
#.#########.###O#O#O###
#...###...#...#OOO#O###
###.###.#.###v#####O###
#...#...#.#.>.>.#.>O###
#.###.###.#.###.#.#O###
#.....###...###...#OOO#
#####################O#

This hike contains 94 steps. (The other possible hikes you could have taken were 90, 86, 82, 82, and 74 steps long.)

Find the longest hike you can take through the hiking trails listed on your map. How many steps long is the longest hike?


"""

"""
Recursion can be minimised by not recursing through single options.
But does that help any? Don't think so...
Visited can be only recorded for crossings.

A propos crissings: can visit only once, can have (T) 3 Neighbors or (x) 4.
Mark all crossings, find their neighbors, record distances.
Then brute-force that travelling salesman.
walk all neighbors recording visited.
Basically same same, but replacing <dist> recursions with one.
"""

from copy import copy
from sys import setrecursionlimit
setrecursionlimit(10000)

def walk(y,x,f,visited):
    global out2
    visited.append([y,x])
    #print()
    #print(visited)
    if y == yend:
        print(out2, len(visited))
        out2 = max(out2, len(visited))
        return
    if f != 'R' and grid[y][x-1] != '#' and [y,x-1] not in visited:
        walk(y,x-1,'L',copy(visited))
    if f != 'L' and grid[y][x+1] != '#' and [y,x+1] not in visited:
        walk(y,x+1,'R',copy(visited))
    if f != 'D' and grid[y-1][x] != '#' and [y-1,x] not in visited:
        walk(y-1,x,'U',copy(visited))
    if f != 'U' and grid[y+1][x] != '#'  and [y+1,x] not in visited:
        walk(y+1,x,'D',copy(visited))
    #print()
    #print(visited)
    return

grid = []
#with open('input--debug') as file:
with open('input') as file:
    for line in file:
        grid.append([])
        for char in line.rstrip():
            grid[-1].append(char)

yend = len(grid)-1
out2 = 0
#print(steps, grid)
walk(1,1,'D',[[0,1]])

print(out2)
# pt 1
# 2402
