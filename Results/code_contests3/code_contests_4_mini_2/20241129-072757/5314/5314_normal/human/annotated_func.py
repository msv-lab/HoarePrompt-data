#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and ai is a list of n integers where each ai (0 ≤ ai ≤ 86400).
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `t` is an integer such that `t` is decreased by the sum of all (86400 - int(a[j])) for j from 0 to `i-1`; `ai` is a list of `n` integers where each `ai` (0 ≤ `ai` ≤ 86400); `a` is a list of strings obtained from `raw_input().split(); `i` is equal to the minimum of `n` and the number of iterations completed, which indicates how many elements were processed from the list `a`.
    print(i)
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 100) and `t` (between 1 and 10^6), and a list `a` containing `n` integers (each between 0 and 86400). It processes the elements of `a` in a loop, subtracting the difference between 86400 and each element from `t` until `t` is no longer positive or all elements of `a` have been processed. It then prints the number of elements processed, which can be at most `n`. If `t` is not sufficient to process all elements, the function will print the number of elements processed until `t` becomes non-positive. The function does not return any value.

