import math
firstline = list(map(int, input().split(" ")))
N = firstline[0]
K = firstline[1]
D = firstline[2]

A = list(map(int, input().split(" ")))

answer = 0
if K == 1:
    for i in A:
        if i > D:
            answer += D
        else:
            answer += i
    print(answer)
else:
    print(min(N, N - K + D))