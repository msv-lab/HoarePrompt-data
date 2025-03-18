#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: After the loop executes all the iterations, `t` must be within the range 1 ≤ t ≤ 10^4, `n`, `a`, and `b` are integers that were input for each iteration of the loop. For each iteration where `n > 1`, `ans1` is `a * n` and `ans2` is `b * n // 2 + a * n % 2`. The final output will be the minimum value between `ans1` and `ans2` for each valid `n > 1`. If `n` is less than or equal to 1, the output for that iteration is simply `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: n, a, and b. For each test case, if n is greater than 1, it calculates two values, ans1 (which is a * n) and ans2 (which is b * n // 2 + a * n % 2), then prints the minimum of these two values. If n is 1 or less, it simply prints the value of a. The function does not return any value but prints the results for each test case.

