# Australian Informatics Olympiad 2019 - RPS

# Input
N = int(input())

Ra, Pa, Sa = map(int, input().split())
Rb, Pb, Sb = map(int, input().split())


# Solve here
ans = 0

for i in range(Ra):
    if Pb > 0:
        Pb -= 1
        ans += 1
    elif Rb > 0:
        Rb -= 1
    else:
        Sb -= 1
        ans -= 1

for i in range(Pa):
    if Sb > 0:
        Sb -= 1
        ans += 1
    elif Pb > 0:
        Pb -= 1
    else:
        Rb -= 1
        ans -= 1
for i in range(Sa):
    if Rb > 0:
        Rb -= 1
        ans += 1
    elif Sb > 0:
        Sb -= 1
    else:
        Pb -= 1
        ans -= 1

print(ans)

