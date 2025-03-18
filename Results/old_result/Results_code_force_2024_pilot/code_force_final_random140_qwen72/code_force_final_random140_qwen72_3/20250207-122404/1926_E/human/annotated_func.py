#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        n_back = n
        
        s = (n + 1) // 2
        
        n = (n + 1) // 2
        
        m = 1
        
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        
        print((2 * (k - (s - n)) - 1) * m)
        
    #State: After the loop executes all iterations, `t` is 0, `_` is `t - 1`, `n` is 1 if it became 0 at any point during the loop, otherwise it is the result of repeatedly halving the initial `n` until it is less than `k`, `n_back` remains the original `n` for each iteration, `s` is `n_back` if `n` became 0 at any point, otherwise it is the sum of the initial `s` and all the values of `n` added during the loop, `m` is \(2^{\text{number of iterations}}\) for each test case, and the final printed value for each test case is \((2 * (k - (s - n)) - 1) * m\).
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, and for each test case, it reads two integers `n` and `k`. It then calculates and prints a specific value based on these inputs. The function does not return any value but outputs the calculated result for each test case. After processing all test cases, the function completes its execution, and the state of the program reflects that all test cases have been processed and the corresponding results have been printed.

