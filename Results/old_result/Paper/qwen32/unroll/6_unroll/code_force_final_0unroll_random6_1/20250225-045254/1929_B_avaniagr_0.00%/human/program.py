for s in [*open(0)][1:]:
    n,k=map(int,s.split())
    print((k//2 + k%2)*(k<(4*n-3)) + (2*n)*(k>=(4*n-3)) + (k==(4*n-2)))