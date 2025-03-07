#State of the program right berfore the function call: a is a list of integers of length n, where 2 <= n <= 50 and 0 <= a_i <= 99 for all 0 <= i < n.
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
        
    #State: `a` is a list of integers, `k` is an input integer, `n` is 8, `x` is 7, `y` is 6, `c` is [1, 2, 3, 4, 5, 6, 7, 8].
    d = sorted(c)
    if (c == d) :
        b.append(1)
    else :
        b.append(0)
    #State: `a` is a list of integers, `k` is an input integer, `n` is 8, `x` is 7, `y` is 6, `c` is [1, 2, 3, 4, 5, 6, 7, 8], `d` is [1, 2, 3, 4, 5, 6, 7, 8]. If `c` is equal to `d`, `b` is a list containing [1]. If `c` is not equal to `d`, `b` is a list containing [0].
#Overall this is what the function does:The function `func_1` reads an integer `k` and a space-separated list of integers `a` from user input. It processes the list `a` to create a new list `c` by potentially splitting each integer greater than 10 into its tens and units digits, and appending them to `c` under certain conditions. The final list `c` is then sorted and compared to the original `c`. If `c` is already sorted, the function appends `1` to a list `b`; otherwise, it appends `0`. The function does not return any value, but modifies the list `b` to contain either `[1]` or `[0]` based on the sorted condition of `c`.

