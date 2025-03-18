#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: Output State: The value of `t` remains an integer such that \(1 \leq t \leq 10^4\), `i` equals `n`, indicating that the loop has completed all its iterations. The variable `n` is the number of times the loop executed, which means `i` ranges from 0 to `n-1`. For each iteration, `a`, `b`, and `c` are integers obtained from the input split, and `d` is calculated as `c / 2`. After executing the if-else block, the output is either `a * b` if it is less than `a * d`, or `round(a * d)` otherwise. The final state does not depend on the specific values of `a`, `b`, and `c` for each iteration but rather on the completion of the loop with `i` equal to `n`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers n, a, and b. It calculates either a * b or round(a * c/2) based on the comparison between a * b and a * c/2, where c is another integer input. After processing all test cases, it outputs the results for each case.

