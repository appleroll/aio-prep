N = int(input())
GOALS = input().split(" ")

TEAM1 = 0
TEAM2 = 0
YES = False

for i in range(N):
    if GOALS[i] == "1":
        TEAM1 +=1
    else:
        TEAM2 +=1
    if (TEAM1 > TEAM2 and YES == False):
        print("YES")
        YES = True

if not YES:
    print("NO")