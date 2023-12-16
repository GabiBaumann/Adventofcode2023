#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 13: Point of Incidence ---

With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.

There's just one problem: you don't see any lava.

You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

123456789
    ><
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><
123456789

In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?

Your puzzle answer was 30705.

--- Part Two ---

You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7

With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7

Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?

"""

"""
The smudge: I check neighboring lines for options -- but need to verify they mirror yet. Which means I need to find candidates again...
Also, finding smudges on non-neighboring lines is done by checking out the candidate rows when they don't play out. Do that on the line-pair giving an error.
"""

grid = []
r_grid = []
cand_h = []
cand_v = []
smudge_h = []
smudge_v = []
out = prev_out = nl = 0
with open('input--debug') as file:
#with open('input') as file:
    image = file.readlines()
    image.append('\n')
    #got_smudge = False
    for line in image:
        if line != '\n':
            if grid and line.strip() == grid[-1]: cand_v.append(nl)
            elif grid: # and not got_smudge:
                print()
                print(grid[-1])
                print(line)
                smc = 0
                for i, c in enumerate(line.strip()):
                    if c != grid[-1][i]:
                        smudge = (nl-1, nl, i, 'v')
                        smc += 1
                if smc == 1: 
                    #got_smudge = True
                    smudge_v.append(smudge)
                    print('We have a smudge.', smudge)
            grid.append(line.strip())
            nl += 1
            continue
        # grid finished, analyse
        nc = len(grid[0])
        nc_half = nc // 2
        nl_half = nl // 2
        # make a grid x->y, y->x
        for col in grid[0]:
            r_grid.append([])
        for row in range(nl):
            for c, col in enumerate(grid[row]):
                r_grid[c].append(col)
        print(grid)
        prev_row = ''
        for c,row in enumerate(r_grid):
            if row == prev_row: cand_h.append(c)
            else: #elif not got_smudge:
                print()
                print(prev_row)
                print(row)
                smc = 0
                for i, char in enumerate(prev_row):
                    if char != row[i]:
                        smudge = (c-1, c, i, 'h')
                        smc += 1
                if smc == 1:
                    #got_smudge = True
                    smudge_h.append(smudge)
                    print('We have a smudge:', smudge)
            prev_row = row

        if not smudge_v and not smudge_h:
            print('Hey, I found no smudge by comparing neighbors!')
            #quit()
        gotit = False
        print(cand_v)
        for cnd in cand_v:
            print('Cnd run 1', cnd)
            nope = False
            if cnd > nl_half:
                print('> nl_half')
                for test_v in range(cnd, nl): # change tests 
                    if grid[test_v] != grid[cnd-(test_v-cnd)-1]:
                        print('Not equal: ', test_v, cnd-(test_v-cnd)-1)
                        nope = True
                        # test for smudge -- and either check for neighbors or drop tests above for neighbors.
                        sc1 = test_v
                        sc2 = cnd-(test_v-cnd)-1
                        smc = 0
                        for i,c in enumerate(grid[sc1]):
                            if c != grid[sc2][i]:
                                smudge = (sc2, sc1,i, 'v')
                                smc += 1
                        if smc == 1:
                            smudge_v.append(smudge)
                            print('We found a smudge:', smudge)
                        break
                    print('Equality of ', test_v, cnd-(test_v-cnd)-1)
                if nope: continue
                if not nope: gotit = True
            else: # cnd <= nl_half)
                print('< nl_half')
                for test_v in range(0, cnd):
                    if grid[cnd+test_v] != grid[cnd-test_v-1]: 
                        print('Not equal: ', cnd+test_v, cnd-test_v-1)
                        nope = True
                        # test for smudge
                        sc1 = cnd+test_v
                        sc2 = cnd-test_v-1
                        smc = 0
                        for i,c in enumerate(grid[sc1]):
                            if c != grid[sc2][i]:
                                smudge = (sc2, sc1, i, 'v')
                                smc += 1
                        if smc == 1:
                            smudge_v.append(smudge)
                            print('We found a smudge', smudge)
                        break
                    print('Equality of: ', cnd+test_v, cnd-test_v-1)
                if nope: continue
                if not nope: gotit = True
            if gotit: outv = cnd
            # break
        if gotit: 
            print('Hrizontal: ', outv)
            out += outv * 100

        # make run conditional on gotit above. Nope, find smudges.
        if True: #not gotit:
            print(cand_h)
            # cand_h computation
            for cnd in cand_h:
                print('Cnd run 2: ', cnd)
                nopeh = False
                if cnd > nc_half:
                    print('> nc_half')
                    for test_h in range(cnd, nc):
                        if r_grid[test_h] != r_grid[cnd-(test_h-cnd)-1]:
                            print('Not equal: ', test_h, cnd-(test_h-cnd)-1)
                            nopeh = True
                            # test for smudge
                            sc1 = test_h
                            sc2 = cnd-(test_h-cnd)-1
                            smc = 0
                            for i,c in enumerate(r_grid[sc1]):
                                if c != r_grid[sc2][i]:
                                    smudge = (sc2, sc1, i, 'h')
                                    smc += 1
                            if smc == 1:
                                smudge_h.append(smudge)
                                print('We found a smudge:', smudge)
                            continue
                        print('Equality of ', test_h, cnd-(test_h-cnd)-1)
                    if not nopeh: gotit = True
                    else: continue
                else:
                    print('< nc_half')
                    for test_h in range(0,cnd):
                        if r_grid[cnd+test_h] != r_grid[cnd-test_h-1]:
                            print('Not equal: ', cnd+test_h, cnd-test_h-1)
                            nopeh = True
                            # test for smudge
                            sc1 = cnd+test_h
                            sc2 = cnd-test_h-1
                            smc = 0
                            for i, c in enumerate(r_grid[sc1]):
                                if c != r_grid[sc2][i]:
                                    smudge = (sc2, sc1, i, 'h')
                                    smc += 1
                            if smc == 1:
                                smudge_h.append(smudge)
                                print('Wf fount a smudge:', smudge)
                            continue
                        print('Equality of: ', cnd+test_h, cnd-test_h-1)
                    if not nopeh: gotit = True
                    else: continue
                if gotit: outh = cnd
                break
            if gotit:
                print('Vertical: ', outh)
                out += outh
        print(smudge_v)
        print(smudge_h)
        grid = []
        r_grid = []
        cand_h = []
        cand_v = []
        nl = 0
        #if out == prev_out:
        #    print('No solution!')
        #    quit()
        #prev_out = out

print(out)

# pt1:
# 2214 is too low.
# 35964 is too high.
# 30705 is right.
