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

m_worth_if_c = 0
m_worths = []

scale = 1
for i in range(N):
    if days[i] == "M":
        m_worth_if_c += scale
    else:
        scale += 1
    m_worths.append(m_worth_if_c + (N - i - 1) * scale)


# Write the answer.
print(max(m_worths))
