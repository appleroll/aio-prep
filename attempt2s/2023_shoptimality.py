import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Shoptimality
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of houses.
N = 0

# M is the number of supermarkets.
M = 0

# H contains the locations of the houses. Note that here the houses are
# numbered starting from 0.
H = []

# S contains the locations of the supermarkets. Note that here the supermarkets
# are numbered starting from 0.
S = []

# P contains the price factors of the supermarkets. Note that here the
# supermarkets are numbered starting from 0.
P = []

# answers[i] should store the badness of the best supermarket for the i-th
# house. Note that here the houses are numbered starting from 0.
answers = []

# Read the values of N, M, H, S and P.
N, M = map(int, input().strip().split())
H = list(map(int, input().strip().split()))
S = list(map(int, input().strip().split()))
P = list(map(int, input().strip().split()))

# TODO: This is where you should compute your solution. For each house, find
# the badness of the best supermarket, and store these values into the list
# answers.

max = H[-1]
cheapest_left = S[0]
for i in range(1, max):
    left_pointer = i

# Write the answers.
for i in range(0, N):
    print(answers[i], end=" ")
print("")
