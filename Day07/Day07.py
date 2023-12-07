#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 7: Camel Cards ---

Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

    32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
    KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?

Your puzzle answer was 241344943.

--- Part Two ---

To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

    32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
    KK677 is now the only two pair, making it the second-weakest hand.
    T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?

"""

hands1 = { 'high':{}, 'pair':{}, 'twopair':{}, 'three':{}, 'fully':{}, 'four':{}, 'five':{} }
hands2 = { 'high':{}, 'pair':{}, 'twopair':{}, 'three':{}, 'fully':{}, 'four':{}, 'five':{} }

with open('input') as file:
    for line in file:
        hand = { 'A':0, 'K':0, 'Q':0, 'J':0, 'T':0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0 }
        hand_raw, bid = line.split()
        for i in range(5):
            hand[hand_raw[i]] += 1
        max1 = max2 = 0
        for i in hand:
            max1 = max(max1, hand[i])
            if i != 'J': max2 = max(max2, hand[i])
        max2 += hand['J']

        # fill dict for pt1
        if max1 == 5:
            hands1['five'][hand_raw] = bid
        elif max1 == 4:
            hands1['four'][hand_raw] = bid
        elif max1 == 3:
            combo = False
            for i in hand:
                if hand[i] == 2: combo = True
            if combo: hands1['fully'][hand_raw] = bid
            else: hands1['three'][hand_raw] = bid
        elif max1 == 2:
            c = 0
            for i in hand:
                if hand[i] == 2:
                    c += 1
            if c == 2:
                hands1['twopair'][hand_raw] = bid
            else:
                hands1['pair'][hand_raw] = bid
        else:
            hands1['high'][hand_raw] = bid

        # fill dict for pt2
        if max2 == 5:
            hands2['five'][hand_raw] = bid
        elif max2 == 4:
            hands2['four'][hand_raw] = bid
        elif max2 == 3:
            combo = False
            for i in hand:
                if hand[i] == 2:
                    if i == 'J':
                        pass # 2 Jokers. Not a fully.
                    elif hand['J'] == 1:
                        # fully w/Joker only by enhancing two pairs.
                        for j in hand:
                            if j != i and hand[j] == 2:
                                combo = True
                    else: combo = True
            if combo: hands2['fully'][hand_raw] = bid
            else: hands2['three'][hand_raw] = bid
        elif max2 == 2:
            c = 0
            for i in hand:
                if hand[i] == 2:
                    c += 1
            if c == 2: # no joker
                hands2['twopair'][hand_raw] = bid
            else: # max 1 joker
                hands2['pair'][hand_raw] = bid
        else: # no joker
            hands2['high'][hand_raw] = bid
                
                
print(hands2)

for t in hands2:
    print(len(hands2[t]))
#quit()
out1 = out2 = rank1 = rank2 = 0

# pt1
for t in hands1:
    lookup = {}
    tosort = []
    for hand in hands1[t]:
        hand_rhex = int(hand.replace('A', 'e').replace('K', 'd').replace('Q', 'c').replace('J', 'b').replace('T', 'a'), 16)
        lookup[hand_rhex] = hand
        tosort.append(hand_rhex)
    tosort.sort()
    for i in tosort:
        rank1 += 1
        out1 += rank1 * int(hands1[t][lookup[i]])

# pt2
for t in hands2:
    lookup = {}
    tosort = []
    for hand in hands2[t]:
        #print(t, hand)
        hand_rhex = int(hand.replace('A', 'e').replace('K', 'd').replace('Q', 'c').replace('J', '1').replace('T', 'a'), 16)
        lookup[hand_rhex] = hand
        tosort.append(hand_rhex)
    tosort.sort()
    for i in tosort:
        rank2 += 1
        out2 += rank2 * int(hands2[t][lookup[i]])
        print(t, hex(i), out2, rank2)

print(out1, out2)

# pt1:
# 285813063 is too high. 
# 241344943
#
# pt2:
# 242823132 is too low.
# 242951033 is too low.
# 243101568 is right.  Missed the 3 with 2 Jokers case before.

# 243140439 is too high. used same joker odering as 1, just to be shure.
#           189406 solutions left to try :D
