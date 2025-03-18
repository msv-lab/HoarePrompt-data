#State of the program right berfore the function call: The function `func` is expected to take two positive integers `n` and `m` as inputs, where 1 <= n, m <= 2 * 10^6. The function should handle multiple test cases, with the number of test cases `t` satisfying 1 <= t <= 10^4. It is guaranteed that the sum of all `n` values and the sum of all `m` values across all test cases do not exceed 2 * 10^6.
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
        
    #State: The function `func` will print the integer value of `ans` for each test case after the loop has finished executing all iterations. The value of `ans` is calculated based on the inputs `n` and `m` for each test case, and the loop iterates `t` times, where `t` is the number of test cases. The variables `n`, `m`, `count`, `countmins`, and `g` are updated within the loop for each test case, but their final values are not retained between test cases.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each of the `t` test cases, it reads two positive integers `n` and `m` from the input, where 1 <= n, m <= 2 * 10^6. It then calculates an integer value `ans` based on the inputs `n` and `m` using a loop that iterates while `count` is less than or equal to `m`. The final value of `ans` is printed for each test case. The function does not return any value, and the variables `n`, `m`, `count`, `countmins`, and `g` are reset for each test case.

