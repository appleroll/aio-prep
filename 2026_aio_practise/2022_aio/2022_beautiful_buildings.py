import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Beautiful Buildings
# 
# Australian Informatics Olympiad 2022
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of buildings.
N = 0

# H contains the heights on the buildings. Note that here the buildings are
# numbered starting from 0.
H = []

answer = 0

# Read the value of N.
N = int(input().strip())

# Read the heights.
H = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the minimum
# ugliness you can achieve into the variable answer.

# Write the answer.
height = 0
ts = 0
for j in range(0, N - 1):
    ts += abs(H[j] - H[j + 1])

possible = []
for i in range(0, N):
    if i == 0:
        possible.append(ts - abs(H[1] - H[0]))
    elif i == N - 1:
        possible.append(ts - abs(H[-1] - H[-2]))
    else:
        if (H[i] < H[i - 1] and H[i] < H[i + 1]) or (H[i] > H[i - 1] and H[i] > H[i + 1]):
            possible.append(ts - 2 * min(abs(H[i] - H[i - 1]), abs(H[i] - H[i + 1])))

# print(ts, possible)

print(min(ts, min(possible)))
        