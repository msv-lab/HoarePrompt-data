for _ in range(int(input())):
    n=int(input())
    s=input()
    f=input()
    c=0
    for i in range(n):
        if s[i]==f[i] and s[i]=='1':
            c+=1
    s1=0
    for i in s:
        if i=='1':
            s1+=1
    f1=0
    for i in f:
        if i=='1':
            f1+=1
    print(max(s1,f1)-c)
    