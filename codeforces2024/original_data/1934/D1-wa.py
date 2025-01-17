import math

def convert_to_num(n):
    ans = 0
    n = n[::-1]
    for i in range(len(n)):
        ans += 2**i * int(n[i])
    return ans

t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    if math.log(n, 2).is_integer():
        print(-1)
    else:
        n = bin(n)[2:]
        m = bin(m)[2:]
        is_there_one = False
        ans = [n]
        a = 0
        for i in range(len(m), 0, -1):
            if n[i] == "1":
                is_there_one = True
                a = i
                break
        if not is_there_one:
            print(-1)
            continue
        
        n1 = convert_to_num(n[a:a + len(m)] + "0"*len(m))
        if convert_to_num(n) ^ n1 == convert_to_num(m):
            print(1)
            print(*[convert_to_num(n), convert_to_num(m)])
        else:
            ans.append(n[a:a + len(m)] + "0"*len(m))
            ans.append(n[a:a + len(m)] + m)
            ans.append(m)
            print(2)
            print(*[convert_to_num(i) for i in ans])
        
        
        
        

