#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is the last integer entered by the user for the nth iteration where 1 ≤ n ≤ 100, `b` is the third integer entered by the user, and `ans1` and `ans2` are defined only if the corresponding `n > 1` during the iterations. If `n > 1`, `ans1` is the product of `a` and `n`, and `ans2` is `b * n // 2 + a * n % 2`. If `n` is not greater than 1, `ans1` and `ans2` remain undefined.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates either \( a \times n \) or \( b \times n / 2 + a \times n \% 2 \) (whichever is smaller), and prints the result. If \( n \) is 1, it simply prints \( a \). After processing all test cases, the function does not return any value but prints the calculated results for each test case.

