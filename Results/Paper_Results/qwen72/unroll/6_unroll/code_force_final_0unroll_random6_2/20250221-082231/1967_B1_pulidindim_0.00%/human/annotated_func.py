#State of the program right berfore the function call: The function `func` is expected to take two positive integers `n` and `m` as inputs, where 1 <= n, m <= 2 * 10^6. The function should handle multiple test cases, with the number of test cases `t` satisfying 1 <= t <= 10^4. The sum of all `n` values and the sum of all `m` values across all test cases should not exceed 2 * 10^6.
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
        
    #State: The function `func` has processed all `t` test cases. For each test case, the final value of `ans` is printed as an integer. The variables `t`, `n`, and `m` retain their initial values, and the loop counter `i` has completed all iterations from 0 to `t-1`. The variable `count` for each test case ends with a value that is either `m + 1` or the value where `g < count - 1` condition breaks the loop.
#Overall this is what the function does:The function `func` processes up to 10,000 test cases, where each test case involves two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). For each test case, it calculates a value `ans` based on the inputs `n` and `m` and prints the final integer value of `ans`. The function ensures that the sum of all `n` and `m` values across all test cases does not exceed 2 * 10^6. After processing all test cases, the function completes and the variables `t`, `n`, and `m` retain their initial values, while the loop counter `i` has completed all iterations from 0 to `t-1`.

