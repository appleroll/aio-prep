import sys, math
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

# TODO: This is where you should compute your solution. Store the minimum total
# amount that Norman must spend into the variable answer.

total_dist_to_end = [0] * N
for i in range(N - 2, -1, -1):
    total_dist_to_end[i] = total_dist_to_end[i + 1] + D[i]

next_cheaper_town = [N] * N
last_seen_pos = {}

for i in range(N - 1, -1, -1):
    current_price = C[i]
    closest_index = N
    # Check all possible prices strictly cheaper than current_price
    for price in range(1, current_price):
        if price in last_seen_pos:
            closest_index = min(closest_index, last_seen_pos[price])
    
    next_cheaper_town[i] = closest_index
    last_seen_pos[current_price] = i

answer = 0
current_inventory = 0

for i in range(N - 1):
    target_town = next_cheaper_town[i]

    if target_town == N:
        required_food = total_dist_to_end[i]
    else:
        required_food = total_dist_to_end[i] - total_dist_to_end[target_town]
        

    target_inventory = min(K, required_food)
    
    if current_inventory < target_inventory:
        cans_to_buy = target_inventory - current_inventory
        answer += cans_to_buy * C[i]
        current_inventory = target_inventory
        
    current_inventory -= D[i]
    
print(answer)
