N, M = map(int, input().split())
team_1 = set()
team_2 = set()
team_1.add(1)
team_2.add(2)

for i in range(M):
    a, b = map(int, input().split())
    if a in team_1:
        team_1.add(b)
    else:
        team_2.add(b)

print(len(team_1), len(team_2))