N = map(int, raw_input().split())[0]
A = map(int, raw_input().split())
kasanari = 1
c = 0
for i in range(0,N-1):
    if A[i]==A[i+1]:
        kasanari = kasanari + 1
    else:
        c = c + kasanari/2
        kasanari = 1
c = c + kasanari/2
print(c)