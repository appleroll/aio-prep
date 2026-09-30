N, K, Q = map(int, input().split())
P = list(map(int, input().split()))
D = list(map(int, input().split()))
closest = [0] * P[-1]
last = P[0]
next = P[0]
next_index = 0

for i in range(P[-1]):
    # print(i, i - last, next - i)
    if i - last > next - i:
        closest[i] = next
    else:
        closest[i] = last
    if i == next:
        last = P[next_index]
        next_index += 1
        next = P[next_index]

        print(i, last, next)

print(closest)
