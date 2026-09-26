n = int(input())
s = input()

max_venom = 0
max_range = n // 5
low = 0

def check(s, x):
    if x == 0:
        return True
    
    # We need to find x of 'S', then 'N', then 'A', then 'K', then 'E' in order
    targets = ['S', 'N', 'A', 'K', 'E']
    t_idx = 0
    found = 0
    
    for char in s:
        if char == targets[t_idx]:
            found += 1
            if found == x:
                t_idx += 1
                found = 0
                if t_idx == 5:
                    return True
    return False

# Binary search for the maximum venom level
while low <= max_range:
    mid = (low + max_range) // 2
    if check(s, mid):
        max_venom = mid
        low = mid + 1
    else:
        max_range = mid - 1

print(max_venom)
