import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Subbookkeeper
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of letters in the word.
N = 0

# word is the word with one missing letter
word = ""

# Read the value of N and the word.
N = int(input().strip())
word = input().strip()

# TODO: This is where you should compute your solution. Store the largest score
# that Rebecca can achieve into the variable answer.
index_of_question = word.index("?")
if index_of_question - 1 < 0:
    possible_combos_with = [word[index_of_question + 1]]
elif index_of_question + 1 >= len(word):
    possible_combos_with = [word[index_of_question - 1]]
else:
    possible_combos_with = [word[index_of_question - 1], word[index_of_question + 1]]

comboes = []

for letter in possible_combos_with:
    tryword = word.replace("?", letter)
    combo = 0
    for i in range(len(tryword)):
        if i == 0:
            continue
        else:
            if tryword[i] == tryword[i - 1]:
                combo += 1
    comboes.append(combo)
    
answer = max(comboes)

# Write the answer.
print(answer)
