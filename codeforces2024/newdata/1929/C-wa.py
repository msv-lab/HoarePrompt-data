from math import ceil
t = int(input())
for qwioercgerhurifeamhv in range(t):
    s = input().split()
    k = int(s[0])
    x = int(s[1])
    a = int(s[2])
    if a > x:
        if x - k > 1:
            print("NO")
        elif -1 < x - k <= 1:
            temp = a - 1
            for i in range(x):
                decrement = ceil((a - temp) / k)
                temp -= decrement
            if temp * k <= a:
                print("NO")
            else:
                print("YES")

        else:
            print("YES")
    else:
        print("NO")
