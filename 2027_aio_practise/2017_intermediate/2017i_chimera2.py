N = int(input())
S1 = input()
S2 = input()
REQUIRED = input()
foiled = False

def a(currently_at):
    times_spliced = 0
    for i in range(N):
        if currently_at == "S1":
            if S1[i] is REQUIRED[i]:
                if currently_at == "S2":
                    times_spliced += 1
                    currently_at = "S1"
            
            elif S2[i] is REQUIRED[i]:
                if currently_at == "S1":
                    times_spliced += 1
                    currently_at = "S2"
            else:
                return False
        else:
            if S2[i] is REQUIRED[i]:
                if currently_at == "S1":
                    times_spliced += 1
                    currently_at = "S2"
            elif S1[i] is REQUIRED[i]:
                if currently_at == "S2":
                    times_spliced += 1
                    currently_at = "S1"
            else:
                return False
    return times_spliced

trys1 = a("S1")
trys2 = a("S2")

if trys1 is not False and trys2 is not False:
    print("SUCCESS")
    print(min(trys1, trys2))
else:
    print("PLAN FOILED")
    
