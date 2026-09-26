details = input().split(" ")
N = int(details[0])
L = int(details[1])

data = []
highest_min = 0
lowest_max = 1000001

for _ in range(N):
    clue = input().split(" ")
    a = int(clue[0])
    b = int(clue[1])

    if a > highest_min:
        highest_min = a
    if b < lowest_max:
        lowest_max = b

if highest_min > lowest_max:
    print(0)
else:
    print(lowest_max - highest_min + 1)
