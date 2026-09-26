import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for TSP
# 
# Australian Informatics Olympiad 2022
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of days.
N = 0

# L contains the minimum number of tomatoes you must sell each day.
L = []

# R contains the maximum number of tomatoes you must sell each day.
R = []

# Read the value of N.
N = int(input().strip())

# Read the values of L and R.
L = list(map(int, input().strip().split()))
R = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. You should output YES
# or NO depending on whether it is possible to meet the requirements. An
# example of how to output YES is shown below.
answer = True

min_tomatoes_today = L[0]
for i in range(1, N):
    if min_tomatoes_today >= L[i] and min_tomatoes_today <= R[i]:
        # dont change
        continue
    else:
        if min_tomatoes_today < L[i]:
            min_tomatoes_today = L[i]
        if min_tomatoes_today > R[i]:
            answer = False


if answer:
    print("YES")
else:
    print("NO")
