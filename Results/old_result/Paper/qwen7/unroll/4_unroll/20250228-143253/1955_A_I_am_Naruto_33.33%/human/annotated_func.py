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
        
    #State: Output State: The output state consists of a series of minimum values printed for each test case. For each test case, if \( n > 1 \), the value printed is the minimum between \( a \times n \) and \( b \times n // 2 + a \times n \% 2 \). If \( n = 1 \), the value printed is simply \( a \). The number of these printed values equals the number of test cases specified by the first input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, a, and b. For each test case, if n is greater than 1, it calculates the minimum value between \(a \times n\) and \(b \times n // 2 + a \times n \% 2\), then prints this minimum value. If n is 1, it simply prints the value of a. The function does not return any value but prints the results for each test case.

