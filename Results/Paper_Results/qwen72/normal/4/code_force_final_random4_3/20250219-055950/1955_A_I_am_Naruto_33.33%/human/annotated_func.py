#State of the program right berfore the function call: t is an integer such that 1 \le t \le {10}^{4}, and for each test case, n, a, and b are integers such that 1 \le n \le 100 and 1 \le a, b \le 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: The loop has executed `t` times, where `t` is an integer such that 1 ≤ t ≤ 10,000. For each of the `t` test cases, `n`, `a`, and `b` are integers provided by the user input, with 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30. If `n` > 1, the minimum of `a * n` and `b * n // 2 + a * n % 2` has been printed. If `n` ≤ 1, `a` has been printed. The values of `t`, `n`, `a`, and `b` remain unchanged outside the loop.
#Overall this is what the function does:The function processes a series of test cases, where each test case involves integers `n`, `a`, and `b` with the constraints \(1 \le n \le 100\) and \(1 \le a, b \le 30\). For each test case, if `n` is greater than 1, it calculates two values: `a * n` and `b * n // 2 + a * n % 2`, and prints the minimum of these two values. If `n` is 1 or less, it simply prints the value of `a`. The function does not return any value; it only prints the results for each test case. After the function concludes, the values of `t`, `n`, `a`, and `b` remain unchanged outside the function.

