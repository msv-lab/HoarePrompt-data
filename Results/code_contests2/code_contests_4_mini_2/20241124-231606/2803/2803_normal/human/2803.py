n,k = map(int,raw_input().split())   
print((2**len(bin(n)[2:])-1) if k-1 else n)
