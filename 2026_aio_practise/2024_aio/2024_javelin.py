import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Javelin
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of students.
N = 0

# D contains the distances. Note that the list starts from 0, and so the values
# are D[0] to D[N-1].
D = []

# Read the value of N and the distances.
N = int(input().strip())
D = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. Store the number of
# current leaders that there were during the competition into the variable
# answer.
answer = 0

current_leader = 0
for i in D:
    if i > current_leader:
        answer += 1
        current_leader = i



# Write the answer.
print(answer)
