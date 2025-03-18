for _ in range(int(input())):
    n = int(input())
    a = input()
    ans = 0
    i = 0
    while i<len(a)-2:
        s = a[i:i+3]
        
        if s == "map" or s == "pie":
            i+=3
            ans+=1
        else:
            i+=1
    print(ans)