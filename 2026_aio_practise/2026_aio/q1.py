a = int(input())
b = list(map(int, input().split(" ")))

dist = 0
for i in range(1, a):
    dist = max(dist, b[i] - b[i - 1])

print(dist)