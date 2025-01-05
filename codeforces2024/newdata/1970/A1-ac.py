s = list(input())
pb=[]
balance=0
for i in range(len(s)):
    pb.append(balance)
    if s[i]=='(':
        balance+=1
    elif s[i]==')':
        balance-=1
mp={}
for i in range(len(s)):
    if pb[i] in mp:
        l=mp[pb[i]]
    else:
        l=[]
    l.append(s[i])
    mp[pb[i]]=l
k=sorted(mp.keys())
for i in range(len(k)):
    for j in range(len(mp[k[i]])-1,-1,-1):
        print(mp[k[i]][j], end='')