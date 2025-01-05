#State of the program right berfore the function call: n is a positive integer less than or equal to 4000, and for each dataset, a, b, c, and d are non-negative integers in the range 0 to 1000 such that a + b + c + d = n. The number of datasets does not exceed 50.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer less than or equal to 4000; `a`, `b`, `c`, and `d` are non-negative integers such that `a + b + c + d = n`; `ans[n]` contains the total count of valid combinations based on the defined conditions; `ans` is a list of size 4001 with the computed values for each `n`.
    exit()
#Overall this is what the function does:The function processes multiple datasets of non-negative integers, where the sum of four integers (a, b, c, and d) equals a positive integer n (≤ 4000). It calculates and prints the total count of valid combinations for each n, based on specified conditions, without accepting any parameters. The function is designed to handle up to 50 datasets. However, it does not return any values; it only prints results for each dataset processed.

