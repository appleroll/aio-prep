line = input().split(" ")
N = int(line[0])
w = int(line[1])


S = [int(input().strip()) for i in range(N)]

prefix_sum = []

first_value = 0
for j in range(w):
    first_value += S[j]
prefix_sum.append(first_value)

for k in range(N - w):
    next_value = prefix_sum[-1] - S[k] + S[k + w]
    prefix_sum.append(next_value)

print(max(prefix_sum))