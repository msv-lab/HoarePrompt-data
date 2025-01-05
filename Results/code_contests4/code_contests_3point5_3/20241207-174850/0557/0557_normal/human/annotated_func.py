#State of the program right berfore the function call: n is a positive integer less than or equal to 4,000. The integers a, b, c, d are in the range 0-1000 and satisfy the equation a + b + c + d = n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer assigned the value of `int(line)`, `ans[n]` is equal to the total count of positive values of `ran` from all iterations, `count` is the sum of all positive values of `ran` from all iterations, `n` is less than or equal to 1000, `a` is equal to the last value assigned in the loop, `e1` is calculated based on the given formula using the last value of `a`, `nab` is decremented `n` times from the last value of `a`. If the loop does not execute, `count` remains 0
    exit()
#Overall this is what the function does:The function func_1 reads input from stdin, calculates four integers a, b, c, and d such that their sum is equal to a positive integer n (<= 4,000) with each integer in the range of 0-1000. It then computes the total count of positive values of 'ran' based on specific conditions and stores it in the ans array. The function prints the calculated count for each input n.

