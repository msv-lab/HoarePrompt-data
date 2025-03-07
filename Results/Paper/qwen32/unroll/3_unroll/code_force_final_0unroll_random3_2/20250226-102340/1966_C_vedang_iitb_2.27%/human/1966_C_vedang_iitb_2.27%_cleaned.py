def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
    return a_new

def func_2(a, n):
    if n == 1:
        return 1
    elif n == 2:
        if a[0] % 2 == 0:
            return 1
        else:
            return 2
    else:
        winNext = func_2(a[1:], n - 1)
        if winNext == 2 or (winNext == 1 and a[0] != 1):
            return 1
        else:
            return 2
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = func_1(a)
    n = len(a)
    if func_2(a, n) == 1:
        print('Alice')
    else:
        print('Bob')