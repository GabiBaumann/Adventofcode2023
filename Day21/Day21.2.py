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

Your puzzle answer was 3716.

--- Part Two ---

The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................

This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

    In exactly 6 steps, he can still reach 16 garden plots.
    In exactly 10 steps, he can reach any of 50 garden plots.
    In exactly 50 steps, he can reach 1594 garden plots.
    In exactly 100 steps, he can reach 6536 garden plots.
    In exactly 500 steps, he can reach 167004 garden plots.
    In exactly 1000 steps, he can reach 668697 garden plots.
    In exactly 5000 steps, he can reach 16733044 garden plots.

However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?

"""
#rounds = 26501365 // 2
rounds = 64
#rounds = 6 # 6: test, 64: pt1,  26501365 (+1 below?): pt 2

seen_odd = {}
seen_even = {}
for i in range(0-rounds, rounds+1):
    seen_odd[i] = []
    seen_even[i] = []
grid = []
vlist_even = [[0, 0]]
seen_even[0].append(0)

with open('input') as file:
#with open('input--debug') as file:
    for line in file.readlines():
        grid.append(line.replace('S', '.').rstrip())
        if 'S' in line:
            y_off = len(grid)
            x_off = 0
            while True:
                x_off += 1
                if line[x_off] == 'S':
                    break
                
maxy = len(grid)
maxx = len(grid[0])

print(maxy, y_off, maxx, x_off, seen_even, vlist_even)
for rnd in range(rounds//2): #32 # ex: 3
    vlist_odd = []
    for seed in vlist_even:
        y,x = seed[:]
        if (x not in seen_odd[y-1]) and grid[(y-1+y_off)%maxy][(x+x_off)%maxx] == '.':
            seen_odd[y-1].append(x)
            vlist_odd.append([y-1,x])
            print('No boulder @', grid[(y-1+y_off)%maxy][(x+x_off)%maxx], y-1+y_off, x+x_off)
        if (x not in seen_odd[y+1]) and grid[(y+1+y_off)%maxy][(x+x_off)%maxx] == '.':
            seen_odd[y+1].append(x)
            vlist_odd.append([y+1, x])
        if (x-1 not in seen_odd[y]) and grid[(y+y_off)%maxy][(x-1+x_off)%maxx] == '.':
            seen_odd[y].append(x-1)
            vlist_odd.append([y,x-1])
        if (x+1 not in seen_odd[y]) and grid[(y+y_off)%maxy][(x+1+x_off)%maxx] == '.':
            seen_odd[y].append(x+1)
            vlist_odd.append([y,x+1])

    vlist_even = []
    for seed in vlist_odd:
        y,x = seed[:]
        if (x not in seen_even[y-1]) and grid[(y-1+y_off)%maxy][(x+x_off)%maxx] == '.':
            seen_even[y-1].append(x)
            vlist_even.append([y-1,x])
        if (x not in seen_even[y+1]) and grid[(y+1+y_off)%maxy][(x+x_off)%maxx] == '.':
            seen_even[y+1].append(x)
            vlist_even.append([y+1, x])
        if (x-1 not in seen_even[y]) and grid[(y+y_off)%maxy][(x-1+x_off)%maxx] == '.':
            seen_even[y].append(x-1)
            vlist_even.append([y,x-1])
        if (x+1 not in seen_even[y]) and grid[(y+y_off)%maxy][(x+1+x_off)%maxx] == '.':
            seen_even[y].append(x+1)
            vlist_even.append([y,x+1])
    print(vlist_even)

out1 = 0
for y in seen_even:
    print(seen_even[y])
    out1 += len(seen_even[y])
    print(out1)

#for y in range(maxy):
#    bla = ''
#    for x in range(maxx):
#        if visited_even[y][x] and grid[y][x] != '#':
#            out1+=1
#            bla += 'O'
#        else: bla += grid[y][x]
#    print(bla)
print(out1)

