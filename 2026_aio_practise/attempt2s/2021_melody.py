import sys
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

# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.

num1dict = {}
num2dict = {}
num3dict = {}

for i in range(0, N, 3):
    num1 = S[i]
    num2 = S[i + 1]
    num3 = S[i + 2]
    if num1 not in num1dict:
        num1dict[num1] = 1
    else:
        num1dict[num1] += 1
    if num2 not in num2dict:
        num2dict[num2] = 1
    else:
        num2dict[num2] += 1
    if num3 not in num3dict:
        num3dict[num3] = 1
    else:
        num3dict[num3] += 1

n1m = max(num1dict, key=num1dict.get)
n2m = max(num2dict, key=num2dict.get)
n3m = max(num3dict, key=num3dict.get)

for i in range(0, N, 3):
    if S[i] != n1m:
        answer += 1
    if S[i + 1] != n2m:
        answer += 1
    if S[i + 2] != n3m:
        answer += 1


# Write the answer.
print(answer)
