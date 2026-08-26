first_line = input().split(" ")
N = int(first_line[0])
K = int(first_line[1])
X = int(first_line[2])

H = [int(x) for x in input().split(" ")]

def buildings():
    seen_heights = set()
    for num_i in range(K,N):
        seen_heights.add(H[num_i - K])
        if (H[num_i] - X in seen_heights) or (H[num_i] + X in seen_heights):
            print("YES")
            return
    print("NO")

buildings()