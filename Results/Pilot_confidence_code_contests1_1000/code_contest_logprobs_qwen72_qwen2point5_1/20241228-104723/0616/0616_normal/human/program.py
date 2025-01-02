import fileinput
def D(a):print(a)
def S(s,I):return int(s.split(" ")[I])
def main():
    z=0
    C=44850
    for l in fileinput.input():
        z+=1
        if(z<2):continue
        I=int(l)
        D("133"+I%C*"7"+298*"3"+I/C*"7")
main()
