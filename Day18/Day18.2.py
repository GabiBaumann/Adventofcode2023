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

Your puzzle answer was 48652.

--- Part Two ---

The Elves were right to be concerned; the planned lagoon would be much too small.

After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.

Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.

So, in the above example, the hexadecimal codes can be converted into the true instructions:

    #70c710 = R 461937
    #0dc571 = D 56407
    #5713f0 = R 356671
    #d2c081 = D 863240
    #59c680 = R 367720
    #411b91 = D 266681
    #8ceee2 = L 577262
    #caa173 = U 829975
    #1b58a2 = L 112010
    #caa171 = D 829975
    #7807d2 = L 491645
    #a77fa3 = U 686074
    #015232 = L 5411
    #7a21e3 = U 500254

Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?

"""

grid = []
gridsize = 600
for y in range(gridsize):
    grid.append([])
    for x in range(gridsize):
        grid[-1].append(0)
y = x = 300
y2 = x2 = miny = minx = maxy = maxx = 0
grid[y][x] = 1
out1 = 1

out2 = 1
inside = 'D' # Ugh... ...could do inside_alt1, inside_alt1...
# D,U for L,R (0,2) in first line, L,R for U,D (3,1) in first line.
#xruns = {0:[0]}
#yruns = {0:[0]}
xruns = {}
yruns = {}
pin = []
print(xruns)
print(type(xruns))
with open('input--debug') as file:
#with open('input') as file:
    for line in file:
        d,l,rgb = line.split()
        l = int(l)
        l2 = int(rgb[2:7], 16)
        d2 = rgb[-2]

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

        # pin.append((y2,x2))
        if d2 == '0': # R
            #for i in range(1, l2+1):
            #    xruns[y2].append(x2+i)
            xruns.update({y2:[x2]})
            x2 += l2
            xruns[y2].append(x2)
            #try: 
            #    if yruns[x2]: pass
            #except: KeyError: yruns.update({x2:[y2]})
        elif d2 == '1': # D
            #for i in range(1, l2+1):
            #    yruns[x2].append(y2+i)
            yruns.update({x2:[y2]})
            y2 += l2
            yruns[x2].append(y2)
            #try: 
            #    if xruns[y2]: pass
            #except KeyError: xruns.update({y2:[x2]})
        elif d2 == '2': # L
            #for i in range(1, l2+1):
            #    xruns[y2].append(x2-i)
            xruns.update({y2:[x2]})
            x2 -= l2
            xruns[y2].append(x2)
            #try: 
            #    if yruns[x2]: pass
            #except: KeyError: yruns.update({x2:[y2]})
        else: # U
            #for i in range(l2+1):
            #    yruns[x2].append(y2-i)
            ### or a mix of walls(y) vs. points(x)?
            yruns.update({x2:[y2]})
            y2 -= l2
            yruns[x2].append(y2)
            #try: 
            #    if xruns[y2]: pass
            #except KeyError: xruns.update({y2:[x2]})
        pin.append((y2,x2)) # once before, oce after the loop.
        out2 += l2 # unless trenches cross/overlap! also, may include in count.

print(out1)
print(out2)
print()
print(xruns)
print(yruns)

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
#### end pt 1

pin.sort()
addup = 0
for c,y in enumerate(pin): # xruns[i].sort()):
    if c%2 == 0: 
        start = y
    else:
        end = y
        
        print(start, end)
        nextrow = 999999999
        for i in pin:
            a,b = i[:]
            if i[1] == start[1]: upto1 = a
            elif i[1] == end[1]: upto2 = a
            if a > start[0]: nextrow = min(nextrow, a)
            #print('tuple disassembly', a,b)
        if nextrow < min(upto1, upto2):
            print('Huh, overlap with up movement')
        addup += min(upto1, upto2,nextrow) * (max(upto1, upto2) - min(upto1, upto2))

        print('y(start):', upto1, 'y(end):', upto2, 'next row:',nextrow, c, addup )




"""
        for i in 


            xs = x
        else:
            xe =x
            # and run...

            for ci, i in enumerate(yruns):
                if not ci%2: 
                    start = i
                else:
                    end = i
                    print('line', x,'yrun',i,'start:', start, yruns[start], 'end:', end, yruns[end])
                #print("line:", x, 'and the downs:', start, end)

"""
print(out1)

for i in xruns:
    print(i)
for i in yruns:
    print(i)
# 3701
# 41810 is too low. (I went into negatives a bit, and stuff did not blow up as I expected :/

# 3708
# 48652 is right. 
