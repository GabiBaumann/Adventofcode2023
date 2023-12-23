#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 17: Clumsy Crucible ---

The lava starts flowing rapidly once the Lava Production Facility is operational. As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.

As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!

You land near the gradually-filling pool of lava at the base of your new lavafall. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.

The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.

To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory. To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

For example:

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533

Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:

2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>

This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?


"""
from sys import setrecursionlimit
setrecursionlimit(40000)

def walk(y,x,p,h):
    h += grid[y][x]
    if visited[y][x] > h:
        visited[y][x] = min(h, visited[endy][endx] - (endy+endx-y-x))
        print('best walk:', visited[endy][endx], y, x, 'now:', visited[y][x], 'with current:', h)
    elif visited[y][x]  < h - 9: # 1 is too little
        return
    if y == endy and x == endx:
        return
    if x < endx and p[-1] != 'L' and p[-3:] != 'RRR':
        walk(y,x+1,p[-2:]+'R',h)
    if y < endy and p[-1] != 'U' and p[-3:] != 'DDD':
        walk(y+1,x,p[-2:]+'D',h)
    if x > 0 and p[-1] != 'R' and p[-3:] != 'LLL':
        walk(y,x-1,p[-2:]+'L',h)
    if y > 0 and p[-1] != 'D' and p[-3:] != 'UUU':
        walk(y-1,x,p[-2:]+'U',h)

#def add(y,x,s,p):
#    sumgrid[y][x] =
    

grid = []
visited = []
sumgrid = []
path = '' #(prefill with '  '?
nowy = nowx = 0

#with open('input--debug') as file:
with open('input') as file:
    for line in file:
        grid.append([])
        visited.append([])
        sumgrid.append([])
        for c in line.rstrip():
            grid[-1].append(int(c))
            visited[-1].append(877)
            sumgrid[-1].append(0)

endy = len(grid) - 1
endx = len(grid[0]) - 1

y = x = 0
loss = 0
# step = 1
sumgrid[0][1] = grid[0][1]
sumgrid[1][0] = grid[1][0]
# step = 2
# 1,1
if sumgrid[0][1] == sumgrid[1][0]:
    path = '..'
    sumgrid[1][1] == sumgrid[0][1] + grid[1][1]
elif sumgrid[0][1] < sumgrid[1][0]:
    path = 'RD'
    sumgrid[1][1] = sumgrid[0][1] + grid[1][1]
else:    
    path = 'DR'
    sumgrid[1][1] = sumgrid[1][0] + grid[1][1]
# 2,0
#D
l = sumgrid[1][0]
# DL
a = sumgrid[1][1] + grid[2][1]
if l == a:
    path = '..'
    sumgrid[2][0] = l + grid[2][0]
elif l < a:
    path = 'DD'
    sumgrid[2][0] = l + grid[2][0]
else:
    sumgrid[2][0] = a + grid[2][0]
# 0,2
#R
a = sumgrid[0][1]
# RU
l = sumgrid[1][1] + grid[1][2]
if l == a:
    path = '..'
    sumgrid[0][2] = l + grid[0][2]
elif l < a:
    path = 'RR'
    sumgrid[0][2] = l + grid[0][2]
else:
    path = 'RD'
    sumgrid[0][2] = a + grid[0][2]
### step = 3
# 2,1
a = sumgrid[1][1]
b = sumgrid[2][0]
l = min(sumgrid[0][2], sumgrid[1][1]) + grid[1][2] + grid[2][2] # (!)

if a == b:
    if a > l:
        path = 'L'
        sumgrid[2][1] = l + grid[2][1]
    else:
        path = '..'
        sumgrid[2][1] = a + grid[2][1]
elif a < b:
    if a > l:
        path = 'L'
        sumgrid[2][1] = l + grid[2][1]
    else:
        path = path + 'D'
        sumgrid[2][1] = a + grid[2][1]
elif b > l:
    path = 'L'
    sumgrid[2][1] = l + grid[2][1]
else: # a>b<l
    path = 'R'
    sumgrid[2][1] = b + grid[2][1]

# 1,2
unfinished = True
a = sgrid[1][1][0]
b = sgrid[0][2][0]
l = sgrid[2][1][0] + grid[2][2]
if (a == l and a <= b) or (b == l) and a >= b):
    ## use l, has wildcard path
    path[1][2] = '.'
    sgrid[1][2].append(l + grid[1][2]
elif a == b and a<=l:
    ## use a, has wildcard path
    path[1][2].append('.')
    sgrid[1][2].append(a + grid[1][2]
elif l > a < b:
    for i, s in enumerate(sgrid[1][1]):
        if l > s < b:
            sgrid[1][2].append(s + grid[1][2])
            path[1][2].append(path[1][1][i] + 'R')
        elif unfinished:
            unfinished = False
            if l < b:
                sgrid[1][2].append(l + grid[1][2])
                path[1][2].append('.')
            else:
                sgrid[1][2].append(b + grid[1][2])
                path[1][2].append('.')
elif l > b < a:
   ... and fix all above . 
if a>=l<=b:
    path = 'D'
    sumgrid[1][2] = l + grid[1][2]
elif a == b:
    path = '..'
    sumgrid[1][2] = a + grid[1][2]
elif a < b:
    path = path + 'R'
    sumgrid[1][2] = a + grid[1][2]
else:
    path = 'D'
    sumgrid[1][2] = b + grid[1][2]

# 3,0
unfinished = True
a = sgrid[2][0][0]
b = sgrid[2][1] + grid[3][1]
if a == b:
    path[3][0].append('.')
    sgrid[3][0].append(sgrid[2][0][0] + grid[3][0])
elif a < b:
    for i,s in enumerate(sgrid[2][0]):
        if s < a:
            sgrid[3][0].append(s + grid[3][0])
            path[3][0].append(path[2][0][i] + 'D')
        elif unfinished:
            unfinished = False
            sgrid[3][0].append(b + grid[3][0])
            path[3][0].append('.'
else:
    path[3][0].append('.') # only ever called from DDD. so...
    sgrid[3][0].append(b + grid[3][0])

# 0,3
for i in grid[:8]:
    print(i[:8])

print()
for i in sumgrid[:4]:
    print(i[:4])
quit()

"""
if a best move n  fails because of path = nnn, consider the left and right
griddum neighbors (which are already computed or computed in move anyway!)
for min extra cost...? can I really apply that or does it need a
quanum superposition to collapse first?
this needs to cosider last step of neighbor to not violate the no turn or step.

hum, pathing:
for every sum with shared minimum (or store second best with other dir / shorter dir as well? ooompf... != dir of best is last entry, An nnn best may store nn and n and !=n for a total of four, if they each are > case before, otherwise perfer othereness < len 1 < len2. 
A wildcard path implies no alternative needed. (1)
len(1) has 1 alternative, always . (2)
len(2) has max 2 alternatives, line above. (3)
len(3) has max 3. line above. (4)
path is wildcard. After every turn, pathlength = 1. 
"""
add(0,1,0,'')
print('\n\n\n\n\n\n\n\n\n\nHalf time!\n\n\n\n\n\n\n\n\n\n')
add(1,0,0,'')

while False:
    y += 1
    l = grid[y][x]
    # here will be dragons
    loss += l
    sumgrid.append[loss]


#for y in range(endy+1):
#    for x in range(endx+1):
#        visited[y][x] = 876 - (endy+endx-y-x)

#visited[0][0] = 0
#walk(0,1,path+'R',0)
#walk(1,0,path+'D',0)

print(visited[endy][endx])

#pt 1:
# 904 is too high. As I subtracted one tile at end, that should be too low.
# So sth keeps me from finding the optimal route. But why? Break at inopportune times? Give 27 points of slack...
# Giving one field (9) of slack helps for test input. Test is right now.
# 876 is still too high. This one came out of a cufoff of visited[yx] < h - 1
# Meanwhile, a run with more slack is still running.
# A call w/ -2 still gives 876, so no. Takes way longer tho...
# Other try and a more efficient one are still running...
