def func_1():
    pass
t = int(input())
while t:
    n = int(input())
    (*inp,) = map(int, input().split())
    la = lb = n + 1
    ans = 0
    for i in inp:
        if i <= la:
            la = i
        elif i <= lb:
            lb = i
        else:
            la = lb
            lb = i
            ans += 1
    print(ans)
    t -= 1