import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Social Distancing
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of meals.
N = 0

# K is the minimum distance between hippos.
K = 0

# D contains the locations of the meals.
D = []

answer = 0

# Read the value of N and K.
N, K = map(int, input().strip().split())

# Read the locations of the meals.
D = [int(input().strip()) for i in range(N)]
D.sort()
# TODO: This is where you should compute your solution. Store the maximum
# number of hippos that can be invited into the variable answer.

last_eaten_dist = 0

for i in range(len(D)):
    if i == 0:
        answer += 1
    else:
        if D[i] - D[last_eaten_dist] >= K:
            answer += 1
            last_eaten_dist = i

# Write the answer.
print(answer)
