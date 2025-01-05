tt=int(input())
for k1 in range(tt):
    n=input()
    s=input()
    cnt=0

    for i in range(len(s)):
        # print(s[i])
        if s[i]=="p":
            f1=0
            f2=0
            if i-2>=0:
                # print(s[i-2]+s[i-1]+s[i])
                if s[i-2]=="m" and s[i-1]=="a":

                    f1=1
            if i+2<=len(s)-1:
                if(s[i+1]=="i" and s[i+2]=="e"):
                    f2=1
            if(f1==1 and f2==1):
                    cnt+=1
            if f1==1 or f2==1:
                    cnt+=1
            # prin(f1)
    print(cnt)