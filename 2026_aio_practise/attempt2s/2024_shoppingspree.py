import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Shopping Spree
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of items.
N = 0

# K is the number of coupons.
K = 0

# costs contains the costs of the items.
costs = []

# Read the value of N, K, and the costs.
N, K = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the minimum cost
# to buy all N items into the variable answer.

answer = 0

for i in range(K):
    answer += costs[i]

for i in range (K, N-K, 2):
    answer += costs[i + 1]


# Write the answer.
print(answer)
