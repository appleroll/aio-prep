import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Distincto's Raffle
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of competitors.
N = 0

# Competitors all submit a number between 1 and K inclusive.
K = 0

# numbers contains the submitted numbers.
numbers = []

# Read the values of N, K and the submitted numbers.
N, K = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the winning
# number, or -1 if there is no winning number, into the variable answer.
distinct = set()
remove_these = set()

for num in numbers:
    if num in distinct:
        remove_these.add(num)
        distinct.remove(num)
    if num not in remove_these:
        distinct.add(num)

if len(distinct) > 0:
    answer = min(distinct)
else:
    answer = -1

# Write the answer.
print(answer)
