#State of the program right berfore the function call: n is a positive integer less than or equal to 4000, and a, b, c, d are non-negative integers such that a + b + c + d = n, with each of a, b, c, and d in the range 0 to 1000. The number of datasets does not exceed 50.
def func_1():
    ans = [0] * 4001
    for line in stdin:
        n = int(line)
        
        if not ans[n]:
            count = 0
            for a in xrange((n if n < 1000 else 1000) + 1):
                e1 = n - a - 1001 if n - a - 1001 >= 0 else -1
                for nab in xrange(n - a, e1, -1):
                    ran = (nab if nab < 1000 else 1000) - (nab - 1001 if nab > 1000
                         else -1)
                    if ran >= 0:
                        count += ran
            ans[n] = count
        
        print(ans[n])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer less than or equal to 4000; `a`, `b`, `c`, `d` are non-negative integers such that `a + b + c + d = n`; `ans[n]` contains the total count of valid combinations calculated during all iterations; `count` is the total calculated based on the iterations for the final value of `n`; `e1` is either `n - 1001` or -1 depending on the value of `a`; `ans` is a list where `ans[i]` holds the calculated count for each integer `i` from 0 to 4000.
    exit()
#Overall this is what the function does:The function processes a list of positive integers `n` (up to 4000) from standard input and calculates the number of valid combinations of non-negative integers `a`, `b`, `c`, and `d` such that `a + b + c + d = n`, with each variable being in the range of 0 to 1000. It stores these counts in an array `ans`, where `ans[n]` holds the count for the corresponding `n`. The function does not directly accept parameters and will continue processing until all datasets are consumed, with a maximum of 50 datasets. If `n` is less than or equal to 4000, it computes and prints the number of valid combinations for each `n` read from input. The function also includes logic to handle cases where the counts may depend on previously computed values in `ans` to avoid redundant calculations.

