l,n=map(int,raw_input().split())
s=str(raw_input())
for i in range (n):
    begin,end=map(int,raw_input().split())
    st=s[begin-1:end]
    arr=[0 for j in range (10)]
    pnt=0
    dir=1
    while (pnt>=0) and (pnt<len(st)):
        if st[pnt].isdigit():
            arr[int(st[pnt])]+=1
            if (int(st[pnt])-1>=0):
                st=st[:pnt]+str(int(st[pnt])-1)+st[pnt+1:]
                pnt+=dir    
            else:
               st=st[:pnt]+st[pnt+1:]
               if dir<0:
                    pnt+=dir
        elif st[pnt]=='>':
            dir=1
            if ((pnt<len(st)-1) and (dir>0) and ((st[pnt+dir]=='>') or (st[pnt+dir]=='<'))) or ((pnt>0) and (dir<0) and ((st[pnt+dir]=='>') or (st[pnt+dir]=='<'))):
                st=st[:pnt]+st[pnt+1:]
            
            pnt+=dir
        elif st[pnt]=='<':
            dir=-1
            if ((pnt<len(st)-1) and (dir>0) and ((st[pnt+dir]=='>') or (st[pnt+dir]=='<'))) or ((pnt>0) and (dir<0) and ((st[pnt+dir]=='>') or (st[pnt+dir]=='<'))):
                st=st[:pnt]+st[pnt+1:]
            
            pnt+=dir
    ss= ' '.join(str(arr).split(','))[1:-1]
    print (ss)
            
                