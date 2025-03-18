#State of the program right berfore the function call: Each test case contains two positive integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The first line of the input contains an integer t (1 ≤ t ≤ 10^4), which is the number of test cases. The sum of n and the sum of m over all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: After processing all test cases, the variable `t` remains unchanged, and the final printed values of `ans` for each test case are the outputs.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two positive integers `n` and `m`, and then computes and prints a specific value `ans` based on these inputs. The value of `ans` is calculated by starting with `n` and adding the integer division of `(n + b)` by `(b * b)` for each `b` from 2 to the minimum of `n` and `m`. This process is repeated for all test cases.

