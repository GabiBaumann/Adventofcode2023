#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your puzzle answer was 54388.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""

with open('input', 'r') as file:
    result1 = result2 = 0
    for line in file:
        digits1 = digits2 = ''
        for char in line:
            if char.isdigit():
                digits1 += char
        for char in line.replace('one','o1e').replace('two','t2').replace('three','3e').replace('four','4').replace('six','6').replace('eight','8').replace('five','5').replace('nine','9').replace('seven','7'):
            if char.isdigit():
                digits2 += char
        result1 += int(digits1[0] + digits1[-1])
        result2 += int(digits2[0] + digits2[-1])

    print(result1, result2)

# pt1:
# 54388

# pt2:
# 53066 is too low. there's overlap: e.g. 'eightwo'. Keep required overlap.
# 53515 it is.
