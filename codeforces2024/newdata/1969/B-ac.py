t = int(input())

for _ in range(t):

    s = input()

    n1 = 0
    ans = 0
    for i in range(len(s)):
        if(s[i]=="1"):
            n1+=1
        else:
            ans += ((n1+1) if(n1!=0) else 0)
    
    print(ans)