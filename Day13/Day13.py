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

def test_rows(c1,c2):
    c = 0
    for i in range(lenx):
        if grid[c1][i] != grid[c2][i]:
            c += 1
    if c == 0:
        return True, False
    elif c == 1:
        return False, True
    return False, False

def test_cols(c1,c2):
    c = 0
    for i in range(leny):
        if grid[i][c1] != grid[i][c2]:
            c += 1
    if c == 0:
        return True, False
    elif c == 1:
        return False, True
    return False, False


grids = [[]]
out1 = out2 = 0

with open('input') as file:
    for line in file:
        if line == '\n':
            grids.append([])
        else:
            grids[-1].append(line.rstrip())

for grid in grids:
    leny = len(grid)
    lenx = len(grid[0])
    print('Next grid.')
    for y in range(leny-1):
        c = 0
        for x in range(lenx):
            if grid[y][x] != grid[y+1][x]:
                c += 1
        if c == 0:
            had_smudge = is_smudge = not_clean = False
            steps = min(y, leny-y-2)
            for step in range(steps):
                clean, smudge = test_rows(y-step-1, y+step+2)
                if smudge:
                    if had_smudge: 
                        is_smudge = False
                        break
                    else: 
                        had_smudge = True
                        is_smudge = True
                if not clean:
                    not_clean = True
                    if not smudge:
                        is_smudge = False
                        break
            if not not_clean:
                print('Clean mirror @y', y-steps, y, y+1, y+steps+1)
                out1 += (y+1) * 100
            elif is_smudge:
                print('Smudge solution @y', y-steps, y, y+1, y+steps+1)
                out2 += (y+1) * 100
        elif c == 1:
            steps = min(y, leny-y-2)
            is_smudge = True
            for step in range(steps):
                clean, smudge = test_rows(y-step-1, y+step+2)
                if smudge:
                    is_smudge = False
                    break
                elif not clean:
                    is_smudge = False
                    break
            if is_smudge:
                print('Smudge on neighbors @y', y-steps, y, y+1, y+steps+1)
                out2 += (y+1) * 100

    for x in range(lenx-1):
        c = 0
        for y in range(leny):
            if grid[y][x] != grid[y][x+1]:
                c += 1
        if c == 0:
            had_smudge = is_smudge = not_clean = False
            steps = min(x, lenx-x-2)
            for step in range(steps):
                clean, smudge = test_cols(x-step-1, x+step+2)
                if smudge:
                    if had_smudge:
                        is_smudge = False
                        break
                    else:
                        had_smudge = True
                        is_smudge = True
                if not clean:
                    not_clean = True
                    if not smudge:
                        is_smudge = False
                        break
            if not not_clean:
                print('Clean mirror @x', x-steps, x, x+1, x+steps+1)
                out1 += x+1
            elif is_smudge:
                print('Smudge solution @x', x-steps, x, x+1, x+steps+1)
                out2 += x+1
        elif c == 1:
            is_smudge = True
            steps = min(x, lenx-x-2)
            for step in range(steps):
                clean, smudge = test_cols(x-step-1, x+step+2)
                if smudge:
                    is_smudge = False
                    break
                elif not clean: # neither nor. No mirror line at all.
                    is_smudge = False
                    break
            if is_smudge:
                print('Smudge on neighbors @x', x-steps, x, x+1, x+steps+1)
                out2 += x+1

print(out1, out2)

# 30705 44615

# pt 2:
# 60483 is too high. Smudge on neighbors works overtime.
# 44615