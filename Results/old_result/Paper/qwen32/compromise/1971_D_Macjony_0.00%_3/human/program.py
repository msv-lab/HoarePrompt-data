t=int(input())
for i in range(t):
    s=input()
    count=1
    flag=False
    j=0
    while j<len(s)-1:
        if s[j]!=s[j+1]:
            count+=1
            if s[j]=="0" and s[j+1]=="1":
                flag=True
                j+=1
        j+=1
    if flag:
        count-=1
    print(count)