N, K, X = map(int, input().split())
H = list(map(int, input().split()))

seen = set()
yes = False

for i in range(K, N):
    seen.add(H[i - K])
    if X + H[i] in seen or H[i] - X in seen:
        print("YES")
        yes = True
        break

if not yes:
    print("NO")