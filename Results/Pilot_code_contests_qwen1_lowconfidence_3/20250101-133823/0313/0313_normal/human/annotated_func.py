#State of the program right berfore the function call: a and c are non-negative integers such that 0 ≤ a, c ≤ 10^9.
def func():
    ans = 0
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    while a > 0 and b > 0:
        ans *= 3
        
        ans += (3 - a % 3 + b % 3) % 3
        
        a //= 3
        
        b //= 3
        
    #State of the program after the loop has been executed: `a` and `b` are both 0, `c` is a non-negative integer such that \(0 \leq c \leq 10^9\), and `ans` is the result of the accumulated updates based on the remainders of `a` and `b` modulo 3.
    print(ans)
#Overall this is what the function does:The function reads two non-negative integers \(a\) and \(b\) from standard input, both within the range \(0 \leq a, b \leq 10^9\). It then iteratively updates a variable `ans` based on the remainders of \(a\) and \(b\) when divided by 3, until both \(a\) and \(b\) become zero. Specifically, in each iteration, `ans` is first multiplied by 3, then incremented by \((3 - a \% 3 + b \% 3) \% 3\). After the loop completes, the function prints the final value of `ans`. The function does not accept any parameters and does not return a value.

