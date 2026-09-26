import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Off the Track
# 
# Australian Informatics Olympiad 2025
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of students.
N = 0
# L is the length of the track.
L = 0

# P contains the locations of the students. Note that the list starts from 0,
# and so the values are P[0] to P[N-1].
P = []

# Read the values of N, L, and the student locations.
N, L = map(int, input().strip().split())
P = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the fewest number
# of seconds you need to end the game into the variable answer.

answer = float('inf')
# Move left
answer = min(answer, P[-1])
# Move right
answer = min(answer, L - P[0])

for i in range(0, N):
    # forwards, then back
    if i != 0:
        answer = min(answer, 2 * (L - P[i]) + P[i - 1])

    # back, the forwards
    if i != N - 1:
        answer = min(answer, P[i] * 2 + (L - P[i + 1]))
        

# Write the answer.
print(answer)
