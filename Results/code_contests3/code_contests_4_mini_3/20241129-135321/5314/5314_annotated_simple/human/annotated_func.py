#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and a is a list of n integers where each integer ai satisfies 0 ≤ ai ≤ 86400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is less than or equal to `0`, `i` is equal to the number of iterations executed which is the minimum of `n` and the number of times `t` can be decremented based on the values in `a`, `a` is a list of `n` integers from input.
    print(i)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100), an integer `t` (1 ≤ t ≤ 10^6), and a list `a` of `n` integers (0 ≤ ai ≤ 86400). It iteratively decrements `t` by the difference of 86400 and the current element of the list `a` until `t` becomes less than or equal to 0 or all elements of `a` have been processed. The function then prints the number of iterations executed, which corresponds to the number of elements processed from `a` before `t` is exhausted or all elements are used. If `t` is insufficient to process all `n` elements in `a`, it will print the count of how many elements were processed before `t` became non-positive.

