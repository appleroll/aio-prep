B, N = map(int, input().split())
A = list(map(int, input().split()))

def balls(k):
    total = 0
    for x in A:
        total += min(x, k)
    return total

lo = 0
hi = max(A)

while lo < hi:
    mid = (lo + hi + 1) // 2

    if balls(mid) < N:
        lo = mid
    else:
        hi = mid - 1

k = lo

used = balls(k)

remaining = N - used

for i in range(B):
    if A[i] > k:
        remaining -= 1

        if remaining == 0:
            print(i + 1)
            break