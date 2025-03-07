t=int(input())
for q in range(t) : 
    a=input()
    b=input()
    kq1=''
    kq2=''
    vt=0
    for i in range(len(a)) : 
        # kiem tra so khac nhau thu 2, bo qua so thu nhat 
        # ki tu nao lon hon se ve ban so khac nhau dau tien be hon
        # so a se la so be , so b se la so lon
        if(a[i]==b[i]): 
            kq1=kq1+a[i]
            kq2=kq2+a[i]
            continue
        else : 
            x,y=min(int(a[i]),int(b[i])),max(int(a[i]),int(b[i]))
            if vt==0 :
                vt=1 
                if a[i] > b[i] :
                    kq1=kq1+str(x)
                    kq2=kq2+str(y)
                else: 
                     kq1=kq1+str(y)
                     kq2=kq2+str(x)
            else : 
                kq1=kq1+str(y)
                kq2=kq2+str(x)
    print(kq1)
    print(kq2)