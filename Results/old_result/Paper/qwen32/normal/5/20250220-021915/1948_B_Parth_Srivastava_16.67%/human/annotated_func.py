#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3. For each test case, n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 99.
def func_1():
    k = int(input())
    a = input()
    a = list(map(int, a.split()))
    x = 0
    y = 0
    n = 0
    c = []
    for i in range(len(a)):
        if a[i] > 10 and i > 0:
            x = int(a[i] % 10)
            y = int(a[i] / 10)
            if y >= c[n - 1]:
                if y <= x:
                    c.append(y)
                    c.append(x)
                    n = n + 2
                else:
                    c.append(a[i])
                    n = n + 1
        elif i == 0 and a[i] > 10:
            x = int(a[i] % 10)
            y = int(a[i] / 10)
            if y <= x:
                c.append(y)
                c.append(x)
                n = n + 2
            else:
                c.append(a[i])
                n = n + 1
        else:
            c.append(a[i])
            n = n + 1
        
    #State: 
    d = sorted(c)
    if (c == d) :
        b.append(1)
    else :
        b.append(0)
    #State: `c` is unchanged, `d` is the sorted version of `c`. If `c` is equal to `d`, `b` has an additional element `1` appended to it. Otherwise, `b` has an additional element `0` appended to it.
#Overall this is what the function does:The function `func_1` reads an integer `k` and a list of integers `a`. It processes the list `a` by potentially splitting two-digit numbers into their tens and units digits under certain conditions, sorts the resulting list, and checks if the original processed list is already sorted. It appends `1` to a list `b` if the processed list is sorted, otherwise it appends `0`.

