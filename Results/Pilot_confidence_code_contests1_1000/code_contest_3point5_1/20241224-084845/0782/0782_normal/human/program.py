t=int(raw_input())
for _ in range(t):
    n=int(raw_input())
    A=map(int,raw_input().split())
    L=map(int,raw_input().split())
    B=[]
    for i in range(n):
        if L[i]==0:
            B.append(A[i])
    B.sort(reverse=True)
    j=0
    for i in range(n):
        if L[i]==0:
            A[i]=B[j]
            j+=1
    print(A)