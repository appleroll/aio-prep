N = int(input())

result = 0

while N >= 100:
    N -= 100
    result += 1
while N >= 20:
    N -= 20
    result += 1
while N >= 5:
    N -= 5
    result += 1
while N >= 1:
    N -= 1
    result += 1
    
print(result)