def proc():
    n,k,pb,ps=map(int, input().split(' '))
    p=list(map(int, input().split(' ')))
    a=list(map(int, input().split(' ')))
    
    pb-=1
    ps-=1
    
    vb=0
    vs=0
    ma_b=0
    ma_s=0
    for i in range(0,n):
        if i>=k: break
        ma_b=max(ma_b, vb+a[pb]*(k-i))
        ma_s=max(ma_s, vs+a[ps]*(k-i))
        
        vb+=a[pb]
        vs+=a[ps]
        pb=p[pb]-1
        ps=p[ps]-1
        
    if ma_b>ma_s: print("Bodya")
    else: 
        if ma_b<ma_s: print("Sasha")
        else: print("Draw")

for _ in range(int(input())): proc()