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

Your puzzle answer was 2402.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

As you reach the trailhead, you realize that the ground isn't as slippery as you expected; you'll have no problem climbing up the steep slopes.

Now, treat all slopes as if they were normal paths (.). You still want to make sure you have the most scenic hike possible, so continue to ensure that you never step onto the same tile twice. What is the longest hike you can take?

In the example above, this increases the longest hike to 154 steps:

#S#####################
#OOOOOOO#########OOO###
#######O#########O#O###
###OOOOO#.>OOO###O#O###
###O#####.#O#O###O#O###
###O>...#.#O#OOOOO#OOO#
###O###.#.#O#########O#
###OOO#.#.#OOOOOOO#OOO#
#####O#.#.#######O#O###
#OOOOO#.#.#OOOOOOO#OOO#
#O#####.#.#O#########O#
#O#OOO#...#OOO###...>O#
#O#O#O#######O###.###O#
#OOO#O>.#...>O>.#.###O#
#####O#.#.###O#.#.###O#
#OOOOO#...#OOO#.#.#OOO#
#O#########O###.#.#O###
#OOO###OOO#OOO#...#O###
###O###O#O###O#####O###
#OOO#OOO#O#OOO>.#.>O###
#O###O###O#O###.#.#O###
#OOOOO###OOO###...#OOO#
#####################O#

Find the longest hike you can take through the surprisingly dry hiking trails listed on your map. How many steps long is the longest hike?

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

def walk_list(o, d, visited):
    global out2
    visited.append(o)
    if o[0] == maxy:
        #print(visited)
        print(out2, d)
        out2 = max(out2, d)
        return
    for dest in salesman[o]:
        tup, dist = dest[:]
        if tup not in visited:
            #print('trying', tup, dist+d)
            walk_list(tup, dist + d, copy(visited))
    return

def build_list(y,x,f,d,o): # y,x, current direction, distance, origin node
    """
    0: v, 1: <, 2: ^, 3: > ...damn. replacing +2 with f itself needed 
    for systematic walk --
    but then -- the recursion shall recurse :)
    """
    if y == maxy:
        salesman[o].append([(y,x),d])
        salesman[(y,x)].append([o, d])
        return
    neighbors = []
    if f != 0 and grid[y-1][x] != '#':
        neighbors.append([y-1,x,2])
    if f != 1 and grid[y][x-1] != '#':
        neighbors.append([y,x-1, 3])
    if f != 2 and grid[y+1][x] != '#':
        neighbors.append([y+1, x, 0])
    if f != 3 and grid[y][x+1] != '#':
        neighbors.append([y,x+1, 1])
    if len(neighbors) == 1: # no crossing, continue
        ty, tx, td = neighbors[0][:]
        build_list(ty,tx,td,d+1,o)
    else: # crossing (T and X)
        if (y,x) in poi:
            if [(y,x),d] not in salesman[o]:
                salesman[o].append([(y,x),d])
            if [o,d] not in salesman[(y,x)]:
                salesman[(y,x)].append([o,d])
            return
        else:
            salesman[(y,x)] = [[o, d]] #.append([o, d]) # new entry
            salesman[o].append([(y,x), d])
            poi.append((y,x))
        for n in neighbors:
            ty, tx, td = n[:]
            build_list(ty,tx,td,1,(y,x))
    return

grid = []
out2 = 0
#with open('input--debug') as file:
with open('input') as file:
    for line in file:
        grid.append(line.rstrip())

maxy = len(grid) - 1
salesman = { (0,1): [], (maxy, len(grid[0])-2): [] }
poi = [(0,1), (len(grid)-1, len(grid[0])-2)]
build_list(1,1,0,1, (0,1))
#print(salesman)
walk_list((0,1),0,[])
print(out2)
# 6450

# pt 1
# 2402
