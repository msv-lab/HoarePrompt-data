#State of the program right berfore the function call: a and c are non-negative integers such that 0 ≤ a, c ≤ 10^9.
def func():
    ans = 0
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    while a > 0 and b > 0:
        ans *= 3
        
        ans += (3 - a % 3 + b % 3) % 3
        
        a //= 3
        
        b //= 3
        
    #State of the program after the loop has been executed: `a` is the result of `(original_a // 27) // 3`, `b` is the result of the original `b` divided by 27, `b` must be greater than 0, `ans` is the sum of `initial_ans + (3 - a % 3 + b % 3) % 3` for each iteration, `a` and `b` are both 0.
    print(ans)
#Overall this is what the function does:The function processes two non-negative integers \(a\) and \(b\) (where \(0 \leq a, b \leq 10^9\)) and calculates a value based on specific arithmetic operations. It repeatedly modifies \(a\) and \(b\) by dividing them by 3 and updating an accumulator `ans` until both \(a\) and \(b\) become zero. Specifically, in each iteration, it updates `ans` by multiplying it by 3 and adding \((3 - a \% 3 + b \% 3) \% 3\). After the loop, the function prints the final value of `ans`. If either \(a\) or \(b\) becomes zero before the other, the remaining value is processed until it reaches zero as well. The function handles edge cases where \(a\) or \(b\) could be zero initially, and it correctly processes the values through multiple iterations of division by 3.

