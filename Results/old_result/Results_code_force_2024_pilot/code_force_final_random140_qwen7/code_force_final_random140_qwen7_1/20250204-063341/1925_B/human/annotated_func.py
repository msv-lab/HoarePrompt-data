#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: Output State: The final value of `ans` will be the maximum value among all divisors of `x` that are less than or equal to `k`, where `k` is `x // n`. After all iterations of the loop, `i` will be the largest divisor of `x` that satisfies the condition `i <= k`. The variable `l` will contain the maximum value found during the loop, along with possibly the value of `i` itself, depending on whether it meets the criteria. 
    #
    #In simpler terms, after the loop has completed all its iterations, `ans` will hold the largest divisor of `x` that is less than or equal to `k`, and `i` will be the last such divisor checked. The list `l` will store the maximum value found during the loop.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it takes two integers \(x\) and \(n\). It calculates the maximum divisor of \(x\) that is less than or equal to \(x \div n\). The function does not return any value but prints the result for each test case.

