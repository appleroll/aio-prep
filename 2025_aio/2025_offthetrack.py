first_line = input().split(" ")
N = int(first_line[0])
L = int(first_line[1])

P = [int(x) for x in input().split(" ")]

# scenario 1: move left
scenario_1 = P[-1]

# scenario 2: move right
scenario_2 = L - P[0]

tp = 1

for i in range(len(P)):
    if i == 0:
        continue
    else:
        if P[i] - P[i-1] > P[tp] - P[tp - 1]:
            tp = i

scenario_3 = 2* (L - P[tp]) + P[tp - 1]
scenario_4 = 2* (P[tp - 1]) + (L - P[tp])

print(min(min(scenario_1, scenario_2), min(scenario_3, scenario_4)))