import sys
from statistics import mode

sys.setrecursionlimit(1000000000)

#
# Solution Template for Melody
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of notes.
N = 0

# K is the largest number which could be a note.
K = 0

# S contains the sequence of notes forming the song.
S = []

answer = 0

# Read the value of N and K.
N, K = map(int, input().strip().split())

# Read each note in the song.
S = [int(input().strip()) for i in range(N)]

split = [S[i:i + 3] for i in range(0, len(S), 3)]

first = [split[i][0] for i in range(0, len(split))]
second = [split[i][1] for i in range(0, len(split))]
third = [split[i][2] for i in range(0, len(split))]

# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.
best_first = mode(first)
best_second = mode(second)
best_third = mode(third)

for seq in split:
    if seq[0] != best_first:
        answer += 1
    if seq[1] != best_second:
        answer += 1
    if seq[2] != best_third:
        answer += 1

# Write the answer.
print(answer)
