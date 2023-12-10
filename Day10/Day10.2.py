#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 10: Pipe Maze ---

You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....

If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....

In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF

In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ

If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....

You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....

In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...

Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

Your puzzle answer was 6886.

--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........

The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....

In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........

In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO

In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?

Your puzzle answer was 371.

"""

"""
|: Pipe N/S
-: Pipe W/E
L: Pipe N/E
J: Pipe N/W
7: Pipe S/W
F: Pipe S/E
.: Ground
S: Start (Pipe hidden)
"""

from sys import setrecursionlimit
setrecursionlimit(15000)

def walk(y, x, outside):
    b = visited[y][x]
    if y == starty and x == startx: return
    if outside == 'left':
        if b == '|':
            if x > 0 and not visited[y][x-1]: visited[y][x-1] = 'X'
            walk(y-1, x, 'left')
        elif b == '7':
            walk(y, x-1, 'down')
        else: # F
            if x > 0 and not visited[y][x-1]: visited[y][x-1] = 'X'
            if y > 0 and x > 0 and not visited[y-1][x-1]: visited[y-1][x-1] = 'X'
            if x > 0 and not visited[y-1][x]: visited[y-1][x] = 'X'
            walk(y, x+1, 'up')
    elif outside == 'right':
        if b == '|':
            if x < xmax and not visited[y][x+1]: visited[y][x+1] = 'X'
            walk(y+1, x, 'right')
        elif b == 'L':
            walk(y, x+1, 'up')
        else: #J
            if x < xmax and not visited[y][x+1]: visited[y][x+1] = 'X'
            if y < ymax and x < xmax and not visited[y+1][x+1]: visited[y+1][x+1] = 'X'
            if y < ymax and not visited[y+1][x]: visited[y+1][x] = 'X'
            walk(y, x-1, 'down')
    elif outside == 'up':
        if b == '-':
            if y > 0 and not visited[y-1][x]: visited[y-1][x] = 'X'
            walk(y, x+1, 'up')
        elif b == 'J':
            walk(y-1, x, 'left')
        else: # 7
            if y > 0 and not visited[y-1][x]: visited[y-1][x] = 'X'
            if y > 0 and x < xmax and not visited[y-1][x+1]: visited[y-1][x+1] = 'X'
            if x < xmax and not visited[y][x+1]: visited[y][x+1] = 'X'
            walk(y+1, x, 'right')
    else: # down
        if b == '-':
            if y < ymax and not visited[y+1][x]: visited[y+1][x] = 'X'
            walk(y, x-1, 'down')
        elif b == 'F':
            walk(y+1, x, 'right')
        else: # L
            if y < ymax and not visited[y+1][x]: visited[y+1][x] = 'X'
            if y < ymax and x > 0 and not visited[y+1][x-1]: visited[y+1][x-1] = 'X'
            if x > 0 and not visited[y][x-1]: visited[y][x-1] = 'X'
            walk(y-1, x, 'left')


def do_next(y, x, p, c):
    h = maze[y][x]
    visited[y][x] = h
    if h == 'S':
        return c
    elif p == 'D': # coming from below
        if h == '|':
            return do_next(y-1, x, 'D', c+1)
        elif h == '7':
            return do_next(y, x-1, 'R', c+1)
        else: #F
            return do_next(y, x+1, 'L', c+1)
    elif p == 'U': # coming from above
        if h == '|':
            return do_next(y+1, x, 'U', c+1)
        elif h == 'J':
            return do_next(y, x-1, 'R', c+1)
        else: #L
            return do_next(y, x+1, 'L', c+1)
    elif p == 'R': # coming from right
        if h == '-':
            return do_next(y, x-1, 'R', c+1)
        elif h == 'F':
            return do_next(y+1, x, 'U', c+1)
        else: #L
            return do_next(y-1, x, 'D', c+1)
    else: # 'L', coming from left
        if h == '-':
            return do_next(y, x+1, 'L', c+1)
        elif h == 'J':
            return do_next(y-1, x, 'D', c+1)
        else: #7
            return do_next(y+1, x, 'U', c+1)
        

maze = open('input').readlines()

ymax = len(maze) - 1
xmax = len(maze[0]) - 2

visited = []
for y in range(ymax+1):
    visited.append([])
    for x in range(xmax+1):
        visited[y].append('')

for y in range(ymax+1):
    for x in range(xmax+1):
        if maze[y][x] == 'S':
            starty = y
            startx = x
            break

# walk the pipe. finished pt 1.
# can I do the marks while walking the pipe?
# yes. Just don't care about given start pos.
if maze[starty-1][startx] in '|7F':
    count = do_next(starty-1, startx, 'D', 1)
elif maze[starty+1][startx] in '|LJ':
    count = do_next(starty+1, startx, 'U', 1)
else: 
    count = do_next(starty, startx-1, 'R', 1)
print(count//2)

# derive pipe for start pos. Do above pipe walk.
if maze[starty-1][startx] in '|7F':
    if maze[starty+1][startx] in '|LJ':
        visited[starty][startx] = '|'
    elif maze[startx][startx-1] in '-LF':
        visited[starty][startx] = 'J'
    else:
        visited[starty][startx] = 'L'
elif maze[starty][startx-1] in '-LF':
    if maze[starty][startx+1] in '-7J':
        visited[starty][startx] = '-'
    else:
        visited[starty][startx] = '7'
else:
    visited[starty][startx] = 'F'


searching = True
for y in range(len(visited)):
    if searching == False: break
    for x in range(len(visited[0])):
        if visited[y][x]:
            starty = y
            startx = x
            searching = False
            break

# walk pipe again, marking outside border tiles.
# start tile is always F.
if not visited[starty][startx-1]: visited[starty][startx-1] = 'X'
if not visited[starty-1][startx-1]: visited[starty-1][startx-1] = 'X'
if not visited[starty-1][startx]: visited[starty-1][startx] = 'X'
walk(starty, startx+1, 'up')

# marking outside. condense.
for x in range(xmax+1):
    if not visited[0][x]:
        visited[0][x] = 'X'
    if not visited[-1][x]:
        visited[-1][x] = 'X'

for y in range(ymax+1):
    if not visited[y][0]:
        visited[y][0] = 'X'
    if not visited[y][-1]:
        visited[y][-1] = 'X'

for y in range(1, ymax+1):
    for x in range(1, xmax+1):
        if not visited[y][x]:
           if visited[y-1][x-1] == 'X' or visited[y-1][x] == 'X' or visited[y-1][x+1] == 'X' or visited[y][x-1] == 'X':
                visited[y][x] = 'X'

for y in range(ymax, 0, -1):
    for x in range(xmax, 0, -1):
        if not visited[y][x]:
            if visited[y+1][x+1] == 'X' or visited[y+1][x] == 'X' or visited[y+1][x-1] == 'X' or visited[y][x+1] == 'X' or visited[y][x-1] == 'X' or visited[y-1][x+1] == 'X' or visited[y-1][x] == 'X' or visited[y-1][x-1] == 'X':
                visited[y][x] = 'X'

out2 = 0
for y in range(len(visited)):
    for x in range(len(visited[0])):
        if not visited[y][x]: out2 += 1

print(count // 2, out2)

# 6886 371

# Both first try. 
# pt 2 took me way too long :/

"""
# visual print
for y in range(len(visited)):
    out = ''
    for x in range(len(visited[0])):
        if visited[y][x]: out += visited[y][x]
        else: 
            out += '*'
    print(y,out)
"""

