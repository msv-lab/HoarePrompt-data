import sys
input = sys.stdin.readline

def readInts():
    return map(int, input().split())

def solve():
    n, m = readInts()
    
    # Convert n and m to binary strings
    s = bin(n)[2:]
    t = bin(m)[2:]
    
    # Pad the binary string of m to match the length of n
    t = '0' * (len(s) - len(t)) + t
    
    # Initialize positions
    x = y = u = -1
    
    # Find the first and second '1' in n, and the first '1' in m
    for i in range(len(s)):
        if s[i] == '1':
            if x == -1:
                x = i
            elif y == -1:
                y = i
        if t[i] == '1' and u == -1:
            u = i

    # Check if transformation is possible
    if y == -1 or x < u < y:
        print(-1)
        return
    elif x == u:
        # Direct transformation possible
        print(1)
        print(n, m)
    else:
        # Calculate the mask value v
        v = (1 << (len(s) - y)) - 1
        if v == m:
            print(1)
            print(n, m)
        else:
            print(2)
            print(n, v, m)
    return

# Read number of test cases
for _ in range(int(input())):
    solve()