#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The value of `t` remains unchanged, and for each iteration of the outer loop, the values of `n` and `m` are updated based on the input provided. The variable `ans` is calculated for each pair of `n` and `m` and printed. After all iterations, the final state of `n` and `m` will be the values from the last input pair, and `ans` will be the last calculated value for that pair.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `m` from the input, where 1 <= n, m <= 2 * 10^6. It then calculates a value `ans` based on `n` and `m` using a specific formula and prints the result. After processing all test cases, the function leaves `t` unchanged, and the final values of `n` and `m` will be those from the last test case. The function does not return any value.

