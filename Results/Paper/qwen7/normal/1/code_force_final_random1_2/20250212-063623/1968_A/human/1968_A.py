from math import gcd
 
n:int = int(input("")) #no.of textcases
for _ in range(n):
    x:int = int(input(""))
    # we need to find y such that
    # 1<=y<x; y = argmax[ gcd(x,y)+y ]
    max = -1
    argmax_y = -1
    for y in range(1,x):
        eq = gcd(x,y) + y
        # print(f"gcd of {x},{y} is {eq-y}")
        if eq>max:
            max=eq
            argmax_y = y
    print(argmax_y)