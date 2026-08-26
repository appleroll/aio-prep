import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Backpacking
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of towns.
N = 0

# K is the maximum number of cans that Norman can fit in his backpack.
K = 0

# D contains the distances between the towns. Note that the list starts from 0,
# and so the values are D[0] to D[N-2].
D = []

# C contains the cost of food in each town. Note that the list starts from 0,
# and so the values are C[0] to C[N-1].
C = []

# Read the values of N, K, D, and C.
N, K = map(int, input().strip().split())
D = list(map(int, input().strip().split()))
C = list(map(int, input().strip().split()))

current_expensive_town = -1
cheapest_towns = []

for i in range(N - 1, 0, -1):
    cheapest_towns[i]



# TODO: This is where you should compute your solution. Store the minimum total
# amount that Norman must spend into the variable answer.

answer = 0

# Write the answer.
print(answer)
