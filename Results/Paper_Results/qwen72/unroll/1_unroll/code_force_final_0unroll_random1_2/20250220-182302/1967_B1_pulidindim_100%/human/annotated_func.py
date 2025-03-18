#State of the program right berfore the function call: The function `func` is expected to take two positive integers `n` and `m` as inputs, where 1 <= n, m <= 2 * 10^6. The function should handle multiple test cases, each with a different pair of `n` and `m`, and the number of test cases `t` is a positive integer such that 1 <= t <= 10^4. The sum of all `n` values and the sum of all `m` values across all test cases do not exceed 2 * 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: The loop has executed `t` iterations, where `t` is the number of test cases. For each test case, the loop reads a pair of integers `n` and `m`, and calculates the value of `ans` based on the provided logic. After all iterations, the final values of `t`, `n`, and `m` remain unchanged, but the variable `ans` will have been printed for each test case, and the variable `count` will have been incremented to `m + 1` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads a pair of positive integers `n` and `m` and calculates a value `ans` based on a specific algorithm. The function then prints the value of `ans` for each test case. After processing all test cases, the function does not return any value, but the final state includes the printed results for each test case, with the variables `t`, `n`, and `m` remaining unchanged.

