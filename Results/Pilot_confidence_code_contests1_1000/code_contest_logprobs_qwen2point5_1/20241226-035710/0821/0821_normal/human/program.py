for _ in range(int(raw_input())):
    n,k=map(int,raw_input().split())
    if k>=n:
        print(k-n)
    else:
        result=n-k
        print(result%2)