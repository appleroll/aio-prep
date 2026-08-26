import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Cookies
#
# Australian Informatics Olympiad 2020
#

# Read input
D, C0 = map(int, input().split())
P1, C1 = map(int, input().split())
P2, C2 = map(int, input().split())

# Write your solution here
cookies_none = C0 * D
cookies_1 = 0
c0_copy = C0

for i in range(D):
    cookies_1 += C0
    if cookies_1 >= P1 and C0 == c0_copy:
        cookies_1 -= P1
        C0 += C1


cookies_2 = 0 

C0 = c0_copy

for i in range(D):
    cookies_2 += C0
    if cookies_2 >= P2 and C0 == c0_copy:
        cookies_2 -= P2
        C0 += C2


C0 = c0_copy
p1_bought = False
p2_bought = False

cookies_3 = 0
for i in range(D):
    cookies_3 += C0
    if not p1_bought:
        if cookies_3 >= P1:
            p1_bought = True
            cookies_3 -= P1
            C0 += C1
    if p1_bought and not p2_bought:
        if cookies_3 >= P2:
            p2_bought = True
            cookies_3 -= P2
            C0 += C2


C0 = c0_copy
p1_bought = False
p2_bought = False

cookies_4 = 0
for i in range(D):
    cookies_4 += C0
    if not p2_bought:
        if cookies_4 >= P2:
            p2_bought = True
            cookies_4 -= P2
            C0 += C2
    if p2_bought and not p1_bought:
        if cookies_4 >= P1:
            p1_bought = True
            cookies_4 -= P1
            C0 += C1



print(max(max(max(cookies_1, cookies_2), max(cookies_3, cookies_none)), cookies_4))