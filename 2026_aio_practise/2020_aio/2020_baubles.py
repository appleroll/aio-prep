import sys

def solve():
    # Read the five input integers from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    RO = int(input_data[0])
    BO = int(input_data[1])
    S  = int(input_data[2])
    RP = int(input_data[3])
    BP = int(input_data[4])
    
    # Condition 1: Fail by running out of potential Red baubles
    if RO + S >= RP and RP > 0:
        destroy_for_red = (RO + S) - RP + 1
    elif RP == 0:
        destroy_for_red = float('inf')
    else:
        destroy_for_red = 0

    # Condition 2: Fail by running out of potential Blue baubles
    if BO + S >= BP and BP > 0:
        destroy_for_blue = (BO + S) - BP + 1
    elif BP == 0:
        destroy_for_blue = float('inf')
    else:
        destroy_for_blue = 0

    # Condition 3: Fail because total baubles drop below total required baubles
    if RO + BO + S >= RP + BP:
        destroy_for_total = (RO + BO + S) - (RP + BP) + 1
    else:
        destroy_for_total = 0

    # Take the absolute minimum actions required to trigger any failure
    ans = min(destroy_for_red, destroy_for_blue, destroy_for_total)
    
    print(ans)

if __name__ == '__main__':
    solve()
