#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 1000, k is an integer such that n - 1 ≤ k ≤ 2n - 2, a, b, c, and d are distinct integers such that 1 ≤ a, b, c, d ≤ n and there is no direct road between a and b, and no direct road between c and d.
def func():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a, b, c, d = map(int, input().split())
    if (n == 4) :
        print('-1')
    else :
        if (k >= n + 1) :
            chain = [a, c]
            for i in range(1, n + 1):
                if i not in [a, b, c, d]:
                    chain.append(i)
                
            #State of the program after the  for loop has been executed: `n` is an integer read from standard input, `k` is an integer read from standard input and is greater than or equal to `n + 1`, `a`, `b`, `c`, and `d` are distinct integers such that 1 ≤ a, b, c, d ≤ n, and there is no direct road between a and b, and no direct road between c and d, `a` is the first integer read from the input, `b` is the second integer read from the input, `c` is the third integer read from the input, `d` is the fourth integer read from the input, `n` is not equal to 4, and `chain` is `[a, c, i1, i2, ..., ik]` where `i1, i2, ..., ik` are the integers from 1 to `n` that are not in `{a, b, c, d}` and are appended in ascending order.
            chain.append(b)
            chain.append(d)
            p1 = list(chain)
            p1[-1], p1[-2] = p1[-2], p1[-1]
            print(' '.join(map(str, p1)))
            p2 = list(chain)
            p2[0], p2[1] = p2[1], p2[0]
            print(' '.join(map(str, p2)))
        else :
            print('-1')
        #State of the program after the if-else block has been executed: *`n` is an integer read from standard input, `k` is an integer read from standard input, `a`, `b`, `c`, and `d` are distinct integers such that 1 ≤ a, b, c, d ≤ n, and there is no direct road between a and b, and no direct road between c and d, `a` is the first integer read from the input, `b` is the second integer read from the input, `c` is the third integer read from the input, `d` is the fourth integer read from the input, and `n` is not equal to 4. If `k` is greater than or equal to `n + 1`, the list `p2` is updated such that its first element is `c` and its second element is `a`, and the string `' '.join(map(str, p2))` has been printed. If `k` is less than `n + 1`, the value `-1` has been printed.
    #State of the program after the if-else block has been executed: *`n` and `k` are integers read from standard input, `a`, `b`, `c`, and `d` are distinct integers such that 1 ≤ a, b, c, d ≤ n, and there is no direct road between a and b, and no direct road between c and d. `a` is the first integer read from the input, `b` is the second integer read from the input, `c` is the third integer read from the input, `d` is the fourth integer read from the input. If `n` is 4, the conditions remain as specified. If `n` is not 4 and `k` is greater than or equal to `n + 1`, the list `p2` is updated such that its first element is `c` and its second element is `a`, and the string `' '.join(map(str, p2))` has been printed. If `n` is not 4 and `k` is less than `n + 1`, the value `-1` has been printed.
#Overall this is what the function does:The function reads two lines of input from standard input. The first line contains two integers, `n` and `k`, and the second line contains four integers, `a`, `b`, `c`, and `d`. The function checks if `n` is 4. If so, it prints `-1`. If `n` is not 4, it further checks if `k` is greater than or equal to `n + 1`. If this condition is true, it constructs a list `chain` starting with `a` and `c`, then appends all integers from 1 to `n` that are not in `{a, b, c, d}`, followed by `b` and `d`. It then creates two lists, `p1` and `p2`, by modifying `chain`. Specifically, `p1` swaps the last two elements of `chain`, and `p2` swaps the first two elements of `chain`. Both `p1` and `p2` are printed as space-separated strings. If `k` is less than `n + 1`, the function prints `-1`. In all cases, the function does not return any value, and the state of the program after the function concludes is that the appropriate output has been printed to the standard output based on the input values.

