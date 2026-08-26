import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Election II
# 
# Australian Informatics Olympiad 2022
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of votes.
N = 0

# votes contains the sequence of votes.
votes = ""

answer = None

# Read the value of N and the votes.
N = int(input().strip())
votes = input().strip()

# TODO: This is where you should compute your solution. Store the winning
# candidate ('A', 'B' or 'C'), or 'T' if there is a tie, into the variable
# answer.

a = 0
b = 0
c = 0
for i in list(votes):
    if i == "A":
        a += 1
    elif i == "B":
        b += 1
    elif i == "C":
        c += 1

if a > b and a > c:
    print("A")
elif b > a and b > c:
    print("B")
elif c > a and c > b:
    print("C")
else:
    print("T")

