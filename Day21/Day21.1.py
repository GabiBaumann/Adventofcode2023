#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 21: Step Counter ---

You manage to catch the airship right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his steps in for the day, and so he'd like to know which garden plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

The Elf starts at the starting position (S) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

Then, he takes a second step. Since at this point he could be at either tile marked O, his second step would allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........

After two steps, he could be at any of the tiles marked O above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........

He will continue like this until his steps for the day have been exhausted. After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........

In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?

"""

#grid = open('input--debug').readlines()
grid = open('input').readlines()
visited_odd = []
visited_even = []
vlist_odd = []
vlist_even = []
nvlist_odd = []
nvlist_even = []
maxy = len(grid)
maxx = len(grid[0])-1

for y,row in enumerate(grid):
    visited_odd.append([])
    visited_even.append([])
    for x,f in enumerate(row.lstrip('\n')):
        if f == 'S':
            visited_even[-1].append(True)
            visited_odd[-1].append(False)
            starty = y
            startx = x
            vlist_even.append([y,x])
        elif f == '#':
            visited_even[-1].append(True)
            visited_odd[-1].append(True)
        else:
            visited_even[-1].append(False)
            visited_odd[-1].append(False)

print(maxy, maxx, starty, startx)

for rnd in range(32): #32 # ex: 3
    for seed in vlist_even:
        y,x = seed[:]
        if y>0 and not visited_odd[y-1][x]:
            nvlist_odd.append([y-1,x])
            visited_odd[y-1][x] = True
        if y<maxy-1 and not visited_odd[y+1][x]:
            nvlist_odd.append([y+1,x])
            visited_odd[y+1][x] = True
        if x>0 and not visited_odd[y][x-1]:
            nvlist_odd.append([y,x-1])
            visited_odd[y][x-1] = True
        if x<maxx-1 and not visited_odd[y][x+1]:
            nvlist_odd.append([y,x+1])
            visited_odd[y][x+1] = True
    vlist_odd = []
    for i in nvlist_odd:
        vlist_odd.append(i)
    nvlist_odd = []
    for seed in vlist_odd:
        y,x = seed[:]
        if y>0 and not visited_even[y-1][x]:
            nvlist_even.append([y-1,x])
            visited_even[y-1][x] = True
        if y<maxy-1 and not visited_even[y+1][x]:
            nvlist_even.append([y+1,x])
            visited_even[y+1][x] = True
        if x>0 and not visited_even[y][x-1]:
            nvlist_even.append([y,x-1])
            visited_even[y][x-1] = True
        if x<maxx-1 and not visited_even[y][x+1]:
            nvlist_even.append([y,x+1])
            visited_even[y][x+1] = True
    vlist_even = []
    for i in nvlist_even:
        vlist_even.append(i)
    nvlist_even = []
    print(vlist_even)

out1 = 0
for y in range(maxy):
    bla = ''
    for x in range(maxx):
        if visited_even[y][x] and grid[y][x] != '#':
            out1+=1
            bla += 'O'
        else: bla += grid[y][x]
    print(bla)
print(out1)

