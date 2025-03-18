#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, which are positive integers such that 1 <= n, m <= 2 * 10^6. The function should be able to handle multiple test cases, where the number of test cases `t` is a positive integer such that 1 <= t <= 10^4. For each test case, `n` and `m` are provided, and the function should calculate the number of ordered pairs (a, b) where 1 <= a <= n, 1 <= b <= m, and a + b is a multiple of b * gcd(a, b).
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
        
    #State: `t` is a specific positive integer provided by the user and must be greater than 0, `i` is `t - 1`, `n` and `m` are integers provided by the user, `count` is `m + 1`, `ans` is the sum of `n` and the series of adjustments made in each iteration of the loop, where each adjustment is calculated as `g / count + 1` and `g` is updated in each iteration to `n / count - (count - 1)`. The loop stops when `g` is less than `count - 1` or when `count` exceeds `m`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads two integers `n` and `m` from the user, and calculates the number of ordered pairs (a, b) where 1 <= a <= n, 1 <= b <= m, and a + b is a multiple of b * gcd(a, b). The function prints the result for each test case. After processing all test cases, the function terminates.

