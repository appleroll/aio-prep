import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Discount Destinations
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of travel days.
N = 0
# K is the window length and D is its spending cap.
K = 0
D = 0
# A contains the undiscounted daily costs. The list starts from 0.
A = []

# Read N, K, D, and the daily costs.
N, K, D = map(int, input().split())
A = list(map(int, input().split()))

paid = [0] * N
window_sum = 0
answer = 0

for i in range(N):
    if i >= K:
        window_sum -= paid[i - K]

    today = min(A[i], D - window_sum)

    paid[i] = today
    window_sum += today
    answer += today

print(answer)


