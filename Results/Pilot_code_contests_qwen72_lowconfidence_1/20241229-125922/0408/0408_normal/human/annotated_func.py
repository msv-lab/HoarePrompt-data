#State of the program right berfore the function call: a is a list of non-negative integers, and k is a positive integer.
def func_1(a, k):
    carry = 1
    for i in range(len(a) - 1, -1, -1):
        newval = a[i] + carry
        
        if newval >= k:
            if i == 0:
                return False
            newval = 0
            carry = 1
        else:
            carry = 0
        
        a[i] = newval
        
    #State of the program after the  for loop has been executed: `a` is a list of non-negative integers where each element has been updated according to the rules defined in the loop. `k` is a positive integer. `carry` is 0 if no overflow occurred during the last update, otherwise, if an overflow occurred at the first element of `a` (index 0), the function returns `False`. If the loop does not execute (i.e., if `a` is an empty list), `carry` remains 1, and the function does not return `False`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a list of non-negative integers `a` and a positive integer `k`. It attempts to increment each element of the list from the end towards the beginning, carrying over values if the sum exceeds or equals `k`. If an overflow occurs at the first element (index 0) of the list, the function returns `False`. Otherwise, it returns `True`. If the list `a` is empty, the function also returns `False` since the loop does not execute, and the initial carry value of 1 causes an immediate overflow condition. After the function concludes, the list `a` is modified in place, reflecting the incremented values, unless an overflow at the first element triggers an early return.

#State of the program right berfore the function call: n, k, and d are integers such that 1 ≤ n, d ≤ 1000 and 1 ≤ k ≤ 10^9.
def func_2():
    n, k, d = map(int, raw_input().split())
    a = [0] * d
    res = list()
    nextFine = True
    for want in xrange(n):
        if not nextFine:
            print(-1)
            return
        
        res.append(list(val + 1 for val in a))
        
        nextFine = func_1(a, k)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 1000, `k` is an integer such that 1 ≤ k ≤ 10^9, `d` is an integer such that 1 ≤ d ≤ 1000, `a` is a list of `d` zeros, `res` is a list containing `n` lists of `d` ones, `nextFine` is the result of the last call to `func_1(a, k)`, `want` is `n - 1`. If `nextFine` becomes `False` at any point during the loop, the loop terminates early, `res` contains fewer than `n` lists, and the program returns `-1`. If `n` is 0, the loop does not execute, and `res` remains an empty list, `nextFine` remains `True`, and `want` is undefined.
    print('\n'.join(' '.join(map(str, l)) for l in res))
#Overall this is what the function does:This function reads three integers `n`, `k`, and `d` from the standard input, where `1 ≤ n, d ≤ 1000` and `1 ≤ k ≤ 10^9`. It initializes a list `a` of `d` zeros and an empty list `res`. The function then iterates `n` times, appending a list of `d` elements (each incremented by 1) to `res` on each iteration. After each append, it calls `func_1(a, k)`, and if `func_1` returns `False`, the function prints `-1` and exits immediately. If the loop completes without `func_1` returning `False`, the function prints each list in `res` on a new line. The function does not return any value explicitly, but it implicitly returns `None` after printing the results. Edge cases include when `n` is 0, in which case the loop does not execute, and `res` remains an empty list, and the function prints nothing.

