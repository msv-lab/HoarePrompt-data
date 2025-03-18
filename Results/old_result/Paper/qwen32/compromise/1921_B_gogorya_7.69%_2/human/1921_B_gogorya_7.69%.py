t = int(input())
 
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
 
    a1 = s1.count("1")
    a2 = s2.count("1")
    hd = a1 - a2
    res = abs(a1 - a2)
    for i in range(n):
        if hd > 0:
            hd -= 1
            continue
        if s1[i] == "1" and s2[i] == "0": res += 1
    print(res)