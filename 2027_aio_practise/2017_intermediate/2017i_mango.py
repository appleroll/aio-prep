Ix, Cx, Id, Cd = map(int, input().split())

locations = [Ix - Id, Cx - Cd, Ix + Id, Cx + Cd]
seen = set()

for i in locations:
    if i in seen:
        print(i)
        break
    else:
        seen.add(i)