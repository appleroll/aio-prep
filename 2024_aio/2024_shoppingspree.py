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
 
pointer_1 = 0
pointer_2 = -1
k_1 =K
k_2 =K
k_3 =K
cost_1 = 0
 
for i in range(int(N/2)):
    pointer_1 = i
    pointer_2 = -1 - i
    if k_1 > 0:
        k_1 -= 1
        cost_1 += costs[pointer_1]
    else:
        cost_1 += costs[pointer_2]
 
cost_2 = 0
 
for i in range(0, N, 2):
    pointer_1 = i
    pointer_2 = i + 1
    if k_2 > 0:
        k_2 -= 1
        cost_2 += costs[pointer_1]
    else:
        cost_2 += costs[pointer_2]

cost_3 = 0

for i in range(N - 1):
    pointer_1 = i
    pointer_2 = i + 1
    if k_3 > 0:
        k_3 -= 1
        cost_3 += costs[pointer_1]
        pointer_2 -= 1

for i in range(K, N - K, 2):
    pointer_1 = i
    pointer_2 = i + 1

    cost_3 += costs[pointer_2]

answer = min(cost_1, cost_2, cost_3)
 
# Write the answer.
print(answer)