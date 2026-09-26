import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Sunday Drive II
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the length of the street.
N = 0
# V contains the volume limits. The list starts from 0.
V = []

# Read the street length and volume limits.
N = int(input().strip())
V = list(map(int, input().strip().split()))
A = [0]
for i in V:
    A.append(i)
V = A

# TODO: Compute the maximum enjoyment and store it in answer.
answer = 0

for i in range(N):
    if V[i + 1] > V[i] + 1:
        V[i + 1] = V[i] + 1

for i in range(N, 0, -1):
    if V[i - 1] > V[i] + 1:
        V[i - 1] = V[i] + 1

V.pop(0)
# Write the answer.
print(sum(V))
