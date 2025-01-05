#State of the program right berfore the function call: n is a positive integer less than or equal to 4000, and a, b, c, and d are non-negative integers such that a + b + c + d = n, with each of a, b, c, and d in the range 0 to 1000. There are at most 50 datasets to process.
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
        
    #State of the program after the  for loop has been executed: `ans[n]` is equal to the total number of ways to partition `n` into four non-negative integers `a`, `b`, `c`, and `d`, with each in the range [0, 1000].
    exit()
#Overall this is what the function does:The function processes multiple datasets, each containing a positive integer `n` (≤ 4000), and calculates the total number of ways to partition `n` into four non-negative integers `a`, `b`, `c`, and `d` such that each integer is in the range [0, 1000] and their sum equals `n`. The results for each dataset are printed. The function does not handle cases where `n` is less than 0 or greater than 4000, nor does it validate the input format or the number of datasets provided.

