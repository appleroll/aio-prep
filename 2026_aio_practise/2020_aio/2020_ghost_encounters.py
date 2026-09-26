from collections import Counter

line = input().split(" ")
N = int(line[0])
K = int(line[1])


G = [input().strip().split(" ") for i in range(N)]
G = [[int(i[0]), int(i[1])] for i in G]

X = [i[0] for i in G]
T = [i[1] for i in G]

stimes = []

for x, t in G:
    stimes.append(t - x * K)

print(Counter(stimes).most_common(1)[0][1])