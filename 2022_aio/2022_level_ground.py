import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Level Ground
# 
# Australian Informatics Olympiad 2022
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of segments.
N = 0

# A contains the altitude of the segments.
A = []

answer = 0

# Read the value of N.
N = int(input().strip())

# Read the altitudes.
A = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the highest
# intensity that can be achieved into the variable answer.
encountered = set()

max_intensity = -1 # you cant go to negative

current_cont = 1

for i in range(len(A)):
    if i == 0:
        continue
    else:
        if A[i] == A[i - 1]:
            # keep streak
            current_cont += 1
        else:
            # broke streak
            max_intensity = max(max_intensity, A[i - 1] * current_cont)
            current_cont = 1
max_intensity = max(max_intensity, A[-1] * current_cont)

# Write the answer.
print(max_intensity)
