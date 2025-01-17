t=int(input())

for i in range(t):
    n=int(input())
    X=[int(x) for x in input().split()]

    A=[0 for j in range(n)]
    A[0]=X[0]+1
    for j in range(1,n):
        while A[j-1]<=X[j-1]:
            A[j-1]+=A[j-2]
        A[j] = X[j-1]+A[j-1]

    for j in A:
        print(j,end=" ")
    print()
