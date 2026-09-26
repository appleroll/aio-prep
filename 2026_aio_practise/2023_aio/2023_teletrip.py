import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for TeleTrip
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading of input and writing of output 
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of instructions.
N = 0

# instructions contains the sequence of instructions.
instructions = ""

# Read the value of N and the instructions.
N = int(input().strip())
instructions = input().strip()

# TODO: This is where you should compute your solution. Store the number of
# different farmhouses that you visit into the variable answer.
visited = set()
visited.add(0)

answer = 1
current_place = 0

for i in list(instructions):
    if i == "L":
        current_place -= 1
    elif i == "R":
        current_place += 1
    elif i == "T":
        current_place = 0
    if current_place not in visited:
        answer += 1
        visited.add(current_place)

# Write the answer.
print(answer)
