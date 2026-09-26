import sys, math
sys.setrecursionlimit(1000000000)

#
# Solution Template for Prime Minister
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of citizens and K is the money available.
N = 0
K = 0
# A contains the citizens' initial wealth in sorted order. The list starts from
# 0.
A = []

# Read N, K, and the initial wealth values.
N, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

# TODO: Compute the maximum possible median wealth and store it in answer.
answer = 0

def valid(num):
    total = 0
    for i in range(N - 1, math.floor(N/2) - 1, -1):
        if A[i] >= num:
            continue
        else:
            total += num - A[i]
            if total > K:
                return False
    return True


low = 0
high = A[-1] + K

while low < high:
    mid = low + (high - low + 1) // 2
    if valid(mid):
        low = mid
    else:
        high = mid - 1

print(low)

