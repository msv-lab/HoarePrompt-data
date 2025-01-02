import fileinput
def D(a):print(a)
def S(s,I):return int(s.split(" ")[I])
def main():
    z=0
    x=0
    for l in fileinput.input():
        z+=1
        if(z<2):continue
        if(z%2==0):
            x="".join(reversed(l[:-1]))
            continue;
        y="".join(reversed(l[:-1]))
        I=0
        while(y[I]=='0'):I+=1
        J=I
        while(x[I]=='0'):I+=1
        D(I-J)
main()
