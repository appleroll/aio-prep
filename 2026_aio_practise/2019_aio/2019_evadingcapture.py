from collections import deque

n, e, x, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# dist[v][p] = shortest distance to v with parity p
dist = [[-1, -1] for _ in range(n + 1)]

queue = deque()

dist[x][0] = 0
queue.append((x, 0))

while queue:
    current, parity = queue.popleft()

    for neighbour in adj[current]:
        new_parity = 1 - parity

        if dist[neighbour][new_parity] == -1:
            dist[neighbour][new_parity] = dist[current][parity] + 1
            queue.append((neighbour, new_parity))

answer = 0

for city in range(1, n + 1):
    if dist[city][k % 2] != -1 and dist[city][k % 2] <= k:
        answer += 1

print(answer)