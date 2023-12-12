#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 12: Hot Springs ---

You finally reach the hot springs! You can see steam rising from secluded areas attached to the primary, ornate building.

As you turn to enter, the researcher stops you. "Wait - I thought you were looking for the hot springs, weren't you?" You indicate that this definitely looks like hot springs to you.

"Oh, sorry, common mistake! This is actually the onsen! The hot springs are next door."

You look in the direction the researcher is pointing and suddenly notice the massive metal helixes towering overhead. "This way!"

It only takes you a few more steps to reach the main gate of the massive fenced-off area containing the springs. You go through the gate and into a small administrative building.

"Hello! What brings you to the hot springs today? Sorry they're not very hot right now; we're having a lava shortage at the moment." You ask about the missing machine parts for Desert Island.

"Oh, all of Gear Island is currently offline! Nothing is being manufactured at the moment, not until we get more lava to heat our forges. And our springs. The springs aren't very springy unless they're hot!"

"Say, could you go up and see why the lava stopped flowing? The springs are too cold for normal operation, but we should be able to find one springy enough to launch you up there!"

There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure which springs would even be safe to use! Worse yet, their condition records of which springs are damaged (your puzzle input) are also damaged! You'll need to help them repair the damaged records.

In the giant field just outside, the springs are arranged into rows. For each row, the condition records show every spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is itself damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.

However, the engineer that produced the condition records also duplicated some of this information in a different format! After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size of its contiguous group (that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2).

So, condition records with no unknown spring conditions might look like this:

#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1

However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1

Equipped with this information, it is your job to figure out how many different arrangements of operational and broken springs fit the given criteria in each row.

In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. The last ? must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? must hide exactly one of the two broken springs. (Neither ?? could be both broken springs or they would form a single contiguous group of two; if that were true, the numbers afterward would have been 2,3 instead.) Since each ?? can either be #. or .#, there are four possible arrangements of springs.

The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run of unknown spring conditions have many different ways they could hold groups of two and one broken springs:

?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#

In this example, the number of possible arrangements for each row is:

    ???.### 1,1,3 - 1 arrangement
    .??..??...?##. 1,1,3 - 4 arrangements
    ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
    ????.#...#... 4,1,1 - 1 arrangement
    ????.######..#####. 1,6,5 - 4 arrangements
    ?###???????? 3,2,1 - 10 arrangements

Adding all of the possible arrangement counts together produces a total of 21 arrangements.

For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. What is the sum of those counts?

"""

def rangetest(s, l, last):
    if (last and len(s) >= l) or len(s) > l+1:
        for i in range(l):
            if s[i] =='.':
                return False
        if not last and len(s) > l:
            if s[l] == '#':
                return False
    return True

def check(s, r):
    if len(r) == 0:
        if '#' in s:
            c = 0
        else: c = 1
    elif len(s) == 0:
        c = 0
    # next step
    elif s[0] == '?':
        # make shure that both branches' results get added.
        # '#': as below, #. make a function for this...
        if rangetest(s[1:], int(r[0])-1, len(r) == 1):
            c = check(s[int(r[0])+1:], r[1:])
        else: c = 0
        """
        if (len(r) == 1 and len(s) >= int(r[0])) or len(s) > int(r[0]) + 1:
            for i in range(1, int(r[0])):
                if s[i] == '.':
                    c = 0
            if len(r) > 1 and len(s) > int(r[0]):
                if s[int(r[0])+1] == '#':
                    c = 0
                else: c = check(s[int(r[0])+1:], r[1:])
            else: c = 0
        else: c = 0
        """
        # '.':
        c += check(s[1:], r)
    elif s[0] == '#':
        # does the group fit into spring string?
        if rangetest(s[1:], int(r[0])-1, len(r) == 1):
            c = check(s[int(r[0])+1:], r[1:])
        else: c = 0
        """
        if (len(r) == 1 and len(s) >= int(r[0])) or len(s) > int(r[0]) + 1:
            for i in range(1, int(r[0])):
                if s[i] == '.':
                    c = 0
            if len(r) > 1 and len(s) > int(r[0]):
                if s[int(r[0])+1] == '#':
                    c = 0
                else: c = check(s[int(r[0])+1:], r[1:])
            else: c = 0
        else: c = 0
        """
    else: # s[0] == '.'
        c = check(s[1:], r)
    return c

out1 = 0
with open('input--debug') as file:
    for line in file:
        spring, report_raw = line.split()
        report = report_raw.split(',')
        
        # walk the entry
        out1 += check(spring, report)
        print(out1)


print(out1)

"""
        impossible = False
        i = b = 0
        while i < len(spring):
            if spring[i] == '.':
                continue #increase i?
            elif spring[i] == '#':
                # does it fit into remaining string?
                fits = False
                if b == len(report) - 1 and i+report[b] < len(spring):
                    fits = True
                elif b < len(report) - 1 and i+report[b] < len(spring) - 2:
                    fits = True
                else:
                    #impossible = True
                    break # continue?
                # does it match the input?
                for s in range(1,report[b]):
                    if spring[i+s] == '.':
                        impossible = True
                if i+s+1 >= len(spring) and b < len(report) - 1:
                    if spring(i+s+1) != '#':
                        i += s+1
                    else:
                        impossible = True
            else: # spring[i] == ?
                # check for . and #
                # .: check(spring[1:], report)
                # #: walk the length of current report + 1 ., check(spring[i+s+1:], report[1:])

            if '#' not in spring[i:] and b == len(report) - 1:
                ## err... do a recursive tree walk with this?
                ## otherwise, futzing with an i_temporal will be needed, no?
                opts += 1
                #continue # ?
            print(spring, report, i, b, opts)    
"""

