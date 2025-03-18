def func_1():
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
    print(n - 2 * neg if n != neg else n)
t = int(input())
while t:
    func_1()
    t -= 1