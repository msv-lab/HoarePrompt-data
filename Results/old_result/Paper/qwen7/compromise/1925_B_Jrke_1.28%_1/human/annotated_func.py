#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: Output State: After the loop executes all its iterations, `x` will be reduced to its smallest prime factor if possible, otherwise `x` will be 1. `n` will be defined and non-zero. `ans` will hold the maximum divisor of `x` that is less than or equal to `k`. The variable `i` will be the last odd number checked before the loop terminates. Since the loop processes each `x` independently, the final state of `ans` will be the maximum of all such maximum divisors found for each `x` processed. The variable `l` is no longer explicitly used but the logic implies that `ans` captures the maximum value from the list of factors considered.
    #
    #In simpler terms, after processing all test cases, `ans` will contain the highest maximum divisor found for any `x` that was less than or equal to `k` for that particular `x`, and `x` will be its smallest prime factor or 1 if no prime factor was found.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(x\) and \(n\). For each \(x\), it finds the largest divisor that is less than or equal to \(k = x // n\). If no such divisor exists, it considers the smallest prime factor of \(x\). The function outputs the maximum of these values found across all test cases.

