a = int(input())
b = list(map(int, input().split(" ")))

first_time_drop = True
yes = True
for i in range(0, a):
    if b[i] > b[i - 1]:
        pass
    else:
        if first_time_drop:
            first_time_drop = False
        else:
            yes = False

if yes:
    print("YES")
else:
    print("NO")
