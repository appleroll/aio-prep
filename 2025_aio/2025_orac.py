import sys, math
sys.setrecursionlimit(1000000000)

#
# Solution Template for ORAC
# 
# Australian Informatics Olympiad 2025
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of informatics problems on ORAC.
N = 0

# D contains the difficulty scores of the problems. Note that the list starts
# from 0, and so the values are D[0] to D[N-1].
D = []

# Read the value of N and the difficulty scores.
N = int(input().strip())
D = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the minimum
# number of mornings you must spend training to solve all N problems into the
# variable answer.
answer = 0

for i in range(N):

    problems_left = N - i

    required_days = D[i] + (problems_left // 2)
  
    answer = max(answer, required_days)

print(answer)
 
