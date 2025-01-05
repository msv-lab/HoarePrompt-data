#State of the program right berfore the function call: k, a, b, and v are integers such that 2 ≤ k ≤ 1000, 1 ≤ a, b, v ≤ 1000.**
def func():
    k, a, b, v = [int(x) for x in raw_input().split()]
    res = 0
    while a > 0:
        res += 1
        
        if b >= k:
            a = a - k * v
            b = b - (k - 1)
        elif b > 0:
            a = a - (b + 1) * v
            b = 0
        else:
            a = a - v
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, and `v` are integers such that 2 ≤ k ≤ 1000, 0 ≤ a ≤ 999, 0 ≤ b ≤ 1000, 1 ≤ v ≤ 1000; `res` is the number of iterations executed by the loop.
    print(res)
#Overall this is what the function does:The function `func` reads input values for k, a, b, and v. It then iterates a loop based on the value of a and updates a, b, and res accordingly. The loop terminates when a becomes non-positive. The function prints the final value of res, which represents the number of iterations executed by the loop. The loop logic involves decrementing a based on conditions related to k, b, and v. The function does not accept any parameters explicitly, and the output is based solely on the input values provided during execution.

