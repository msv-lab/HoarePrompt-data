from math import sqrt;

def check(a, b, cc):
    cc1 = int(cc);
    while (cc1%a==0):
        cc1 //= a;
    while (cc1%b==0):
        cc1 //= b;
    while (cc%b==0):
        cc //= b;
    while (cc%a==0):
        cc //= a;
    if cc == 1 or cc1 == 1:
        return True;
    return False;

for _ in range (int(input())):
    a, b, l = map(int, input().split());
    u = 0;
    div = [];
    for i in range (1, int(sqrt(l))+1):
        if l%i==0:
            div.append(i); div.append(l//i);
    div = sorted(list(set(div)));
    ll = [];
    for i in div:
        if i == l:
            u += 1;
        else:
            cc = l//i; 
            if check(a, b, cc): u += 1;
    print (u);