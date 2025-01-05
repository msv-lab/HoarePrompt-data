#State of the program right berfore the function call: n is a positive integer less than or equal to 4,000. a, b, c, and d are integers in the range 0-1000 such that a + b + c + d = n.
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
        
    #State of the program after the  for loop has been executed: `n`, `a`, `b`, `c`, `d` are integers, `a + b + c + d = n`, `ans` is a list of 4001 elements filled with the sum of valid `ran` values for each index in the list.
    exit()
#Overall this is what the function does:The function `func_1` reads input from stdin, calculates the sum of `ran` values for each index in the `ans` list based on the constraints provided, and prints the calculated sum. The function does not accept any parameters, and the output postcondition is not specified.

