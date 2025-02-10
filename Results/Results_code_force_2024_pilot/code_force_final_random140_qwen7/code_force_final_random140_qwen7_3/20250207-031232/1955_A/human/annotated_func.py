#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: Output State: The loop will continue to execute until all test cases specified by the initial integer `t` have been processed. After all iterations, the following will be true:
    #
    #- `t` will be the initial input integer specifying the number of test cases.
    #- For each test case, `n`, `a`, and `b` will hold the most recent values entered by the user during that iteration.
    #- `s1` will be the value of `n * a` for the last processed test case.
    #- `s2` will be the value of `b * (n // 2) + n % 2 * a` for the last processed test case.
    #- The final output will be the minimum of `s1` and `s2` for the last processed test case, printed for each test case as the loop progresses.
    #
    #This means that after all iterations, the output will consist of the minimum values of `s1` and `s2` calculated for each of the `t` test cases, printed one per line in the order they were processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( t \), \( n \), \( a \), and \( b \). It calculates two expressions, \( s1 = n \times a \) and \( s2 = b \times (n // 2) + n \% 2 \times a \), for each test case and prints the minimum of these two values. After processing all test cases, the function outputs the minimum values of \( s1 \) and \( s2 \) for each test case, one per line, in the order they were processed.

