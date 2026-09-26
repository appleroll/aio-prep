import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Tennis Robot II
# 
# Australian Informatics Olympiad 2024
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of bins.
N = 0

# M is the number of instructions.
M = 0

# X contains the number of balls in each bin. Note that this list starts from 1
# (not 0), and so the values are X[1] to X[N].
X = []

# A and B contain the instructions. Note that the lists start from 0, and so
# the instructions are (A[0], B[0]) to (A[M-1], B[M-1]).
A = []
B = []

# Read the values of N, M, X, A, and B.
N, M = map(int, input().strip().split())

# Values in X are indexed from 1 to N (not 0 to N-1)
X = [0] + list(map(int, input().strip().split()))

for i in range(0, M):
    input_vars = list(map(int, input().strip().split()))
    A.append(input_vars[0])
    B.append(input_vars[1])

# Compute the solution.
answer = 0

# Step 1: Simulate the first round completely
crashed = False
for j in range(M):
    u = A[j]
    v = B[j]
    if X[u] == 0:
        answer = j
        crashed = True
        break
    X[u] -= 1
    X[v] += 1

if not crashed:
    # Step 2: Calculate net decrease (D) and max temporary drop (E) per round
    D = [0] * (N + 1)
    E = [0] * (N + 1)
    current_drop = [0] * (N + 1)
    
    for j in range(M):
        u = A[j]
        v = B[j]
        E[u] = max(E[u], current_drop[u])
        current_drop[u] += 1
        current_drop[v] -= 1
        
    for i in range(1, N + 1):
        D[i] = current_drop[i]

    # Identify candidate Type 2 bins
    type_2_bins = [i for i in range(1, N + 1) if D[i] > 0]

    if not type_2_bins:
        answer = -1
    else:
        # Step 3: Find the minimum number of additional full rounds survived
        # X[i] currently holds the ball count at the end of round 1
        min_rounds_survived = float('inf')
        for i in type_2_bins:
            # Bins crash when remaining balls fall below E[i] + 1
            rounds_survived = (X[i] - E[i] - 1) // D[i] + 1
            if rounds_survived < min_rounds_survived:
                min_rounds_survived = rounds_survived
        
        # Step 4: Fast forward to the beginning of the crash round
        for i in range(1, N + 1):
            X[i] -= min_rounds_survived * D[i]
            
        # Step 5: Simulate the final crash round
        total_instructions_before = M + min_rounds_survived * M
        for j in range(M):
            u = A[j]
            v = B[j]
            if X[u] == 0:
                answer = total_instructions_before + j
                break
                
            X[u] -= 1
            X[v] += 1

# Write the answer.
if answer == -1:
    print("FOREVER")
else:
    print(answer)
