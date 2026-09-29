N = int(input())
A = list(map(int, input().split()))

b = set()

d = {}

deliciousness = 0

for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
right = len(d)
left = 0

for i in range(N - 1):
    # add to left piece
    if A[i] not in b:
        b.add(A[i])
        left += 1

    d[A[i]] -= 1
    if d[A[i]] == 0:
        right -= 1
    deliciousness = max(deliciousness, left + right)


print(deliciousness)