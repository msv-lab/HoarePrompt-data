#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: `t` is the number of test cases, `i` is `t`, `n` and `m` are the values from the last test case, `count` is the final value that caused the inner loop to terminate for the last test case, `ans` is the final result printed for the last test case, `countmins` is `count - 1` for the last iteration of the last test case, and `g` is `n / count - countmins` for the last iteration of the last test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two positive integers `n` and `m`. For each test case, it calculates and prints a result based on a specific computation involving `n` and `m`. The result is an integer value derived from the iterative process described in the code.

