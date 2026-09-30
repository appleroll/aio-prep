Xt, Yt = map(int, input().split())
Xc, Yc = 0

answer = ""
there = False

while not there:
    if Xt > Xc and Yt > Yc:
        # Move NE diagonal (1, 1)
        answer += "RL"
        Xc += 1
        Yc += 1
    if Xt < Xc and Yt > Yc:
        # Move NW diagonal (-1, 1)
        answer += "LR"
        Xc -= 1
        Yc += 1
    if Xt < Xc and Yt < Yc:
        # Move SW diagonal (-1, -1)
        answer += "LL"
        Xc -= 1
        Yc -= 1
    if Xt > Xc and Yt > Yc:
        # Move SE diagonal (1, -1)
        answer += "RR"
        Xc += 1
        Yc -= 1
        

