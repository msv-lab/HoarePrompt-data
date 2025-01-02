import fileinput
def D(a):print(a)
def S(s,I):return int(s.split(" ")[I])
def main():
    z=0
    N=0
    A=0
    I=0
    o=0
    for l in fileinput.input():
        z+=1
        if(z<2):N=int(l)
        else: A=map(int,l.split(" "))
    for i in range(N):A[i]=abs(A[i])
    A.sort()
    for i in range(N):
        while(I<N and A[i]*2>=A[I]):I+=1
        o+=I-i-1
    D(o)
main()
