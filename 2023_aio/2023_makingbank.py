import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Making Bank
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of days.
N = 0

# days contains the type of each day.
days = ""

# Read the value of N and the string of characters.
N = int(input().strip())
days = input().strip()

# TODO: This is where you should compute your solution. Store the most money
# that you can retire with into the variable answer.

answer = 0
s = 1

remaining_c = days.count("C")
remaining_m = days.count("M")

for i in range(N):
    cm = remaining_c + remaining_m
    benefit_of_learning = (cm - 1) * (s + 1)
    benefit_of_painting = cm * s

    if days[i] == "C" and benefit_of_learning > benefit_of_painting:
        s += 1
    else:
        answer += s

    if days[0] == "C":
        remaining_c -= 1
    if days[0] == "M":
        remaining_m -= 1



# Write the answer.
print(answer)
