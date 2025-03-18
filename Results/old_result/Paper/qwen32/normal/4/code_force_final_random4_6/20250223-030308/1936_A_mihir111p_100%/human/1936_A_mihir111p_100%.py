def find(a,b,c,d):
    print("?",a,b,c,d)
    return input()
    
for _ in range(int(input())):
    n = int(input())
    ans1 = 0
    for i in range(1,n):
        x = find(ans1,ans1,i,i)
        if x == "<":
            ans1 = i
    mx = 0
    v = [0]
    # print(ans1)
    for i in range(1,n):
        x = find(mx,ans1,i,ans1)
        if x == "<":
            v = []
            mx = i
            v.append(i)
        elif x =="=":
            v.append(i)
    mx= v[0]
    # print(v)
    ans = v[0]
    for i in range(1,len(v)):
        x = find(ans,ans,v[i],v[i])
        if x == ">":
            ans = v[i]
    print("!", ans,ans1)