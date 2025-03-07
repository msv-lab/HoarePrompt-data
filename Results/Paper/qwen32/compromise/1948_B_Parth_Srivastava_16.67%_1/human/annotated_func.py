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
        
    #State: t is an integer such that 1 <= t <= 10^3; n is 9; a is a list of integers derived from the input string; k is an input integer; x is 9; y is 8; c is [1, 2, 3, 4, 5, 6, 7, 8, 9].
    d = sorted(c)
    if (c == d) :
        b.append(1)
    else :
        b.append(0)
    #State: `t` is an integer such that 1 <= t <= 10^3; `n` is 9; `a` is a list of integers derived from the input string; `k` is an input integer; `x` is 9; `y` is 8; `c` is [1, 2, 3, 4, 5, 6, 7, 8, 9]; `d` is [1, 2, 3, 4, 5, 6, 7, 8, 9]; if `c` is equal to `d`, then `b` has an additional element `1` appended to its previous contents. Otherwise, `b` has an additional element `0` appended to it.
#Overall this is what the function does:The function `func_1` processes a list of integers derived from the input, rearranges certain elements based on specific conditions, and appends either `1` or `0` to a list `b` depending on whether the rearranged list is sorted.

