L = map(int, raw_input().split())
n = L[0]
x = L[1]
res = n
a = x
b = n-x
flag = True
while flag :
    if a > b:
        q = a // b
        a -= q*b
        res += 2*q*b
    elif  b > a:
        q = b // a
        b -= q*a
        res += 2*a*q
    else:
        res += a
        flag = False
print(res)