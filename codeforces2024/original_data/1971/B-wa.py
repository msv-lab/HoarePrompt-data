for _ in range(int(input())):
    k=input()
    s=[]
    for i in k:
        if i not in s:
            s.append(i)
    if len(s)<=1:
        print("NO")
    else:
        print("YES")
        print(k[::-1])