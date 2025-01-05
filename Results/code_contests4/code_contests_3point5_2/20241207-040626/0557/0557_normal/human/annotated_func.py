#State of the program right berfore the function call: n is a positive integer less than or equal to 4,000. a, b, c, d are integers in the range 0-1000 and satisfy the equation a + b + c + d = n.
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
        
    #State of the program after the  for loop has been executed: The value stored in `ans` at index `n` contains the sum of all positive `ran` values calculated in each iteration of the loop for all valid values of `n`. All other variables retain their values as described in the code.
    exit()
#Overall this is what the function does:The function `func_1` reads input from stdin, calculates four integers `a`, `b`, `c`, `d` in the range 0-1000 that satisfy the equation a + b + c + d = n, where n is a positive integer less than or equal to 4,000. The function then stores the calculated sum in the `ans` list at index `n` and prints it. The function does not actually return the calculated integers `a`, `b`, `c`, `d` as mentioned in the annotations, and it exits after processing all input.

