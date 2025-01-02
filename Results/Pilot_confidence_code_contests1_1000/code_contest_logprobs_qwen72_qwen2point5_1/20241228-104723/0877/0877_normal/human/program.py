rr=raw_input
rrI = lambda: int(rr())
rrM = lambda: map(int,rr().split())
debug=0
if debug:
    fi = open('t.txt','r')
    rr=lambda: fi.readline().replace('\n','')

N=rrI()
N-=1
A,B = rr(),rr()
cd = [N-1,0]
dirs = zip('NEWS','SWEN')
def do2(X):
    for i in X:
        Ac1 = A[cd[0]]
        for d1,d2 in dirs:
            if Ac1 == d1 and i == d2:
                if cd[0] > 0: cd[0] -= 1
    cd[1] = N-1

last = 0
while 1:
    do2(B[last:])
    if cd == [last,N-1]:
        good = 0
        break
    if cd == [N-1,N-1]:
        good = 1
        break
    last = cd[0]
    A,B = B,A
    cd = cd[::-1]
    
print ["NO","YES"][good]
