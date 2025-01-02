#State of the program right berfore the function call: k is a positive integer (1 ≤ k ≤ 10^18), a and b are integers representing the initial choices of Alice and Bob respectively (1 ≤ a, b ≤ 3). The matrices A and B are 3x3 matrices of integers (1 ≤ Ai, j, Bi, j ≤ 3) representing the choices of Alice and Bob in the next game based on their previous choices.
def func():
    f = lambda : list(map(int, raw_input().split()))
    g = lambda : [[0] * 4] + [([0] + f()) for i in range(3)]
    h = lambda x, y: x - 1 == y % 3
    t = lambda a, b, u, v: (A[a][b], B[a][b], u + h(a, b), v + h(b, a))
    k, a, b = f()
    p = 2520
    s, d = divmod(k, p)
    A, B = g(), g()
    u = v = x = y = 0
    for j in range(d):
        a, b, u, v = t(a, b, u, v)
        
    #State of the program after the  for loop has been executed: `k` is an input integer, `a` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `b` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `u` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `v` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `p` is 2520, `s` is `k // 2520`, `d` is `k % 2520`, `A` is a 3x3 matrix of integers where each row is prepended with `0` and contains integers read from input, `B` is a 3x3 matrix of integers where each row is prepended with `0` and contains integers read from input, `x` is 0, `y` is 0, `j` is `k % 2520 - 1`.
    for i in range(p):
        a, b, x, y = t(a, b, x, y)
        
    #State of the program after the  for loop has been executed: `k` is an input integer, `a` is the result of applying the function `t` to the initial values of `a`, `b`, `x`, and `y` for `p` times, `b` is the result of applying the function `t` to the initial values of `a`, `b`, `x`, and `y` for `p` times, `x` is the result of applying the function `t` to the initial values of `a`, `b`, `x`, and `y` for `p` times, `y` is the result of applying the function `t` to the initial values of `a`, `b`, `x`, and `y` for `p` times, `u` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `v` is the result of applying the function `t` to the initial values of `a`, `b`, `u`, and `v` for `k % 2520` times (or remains the initial value if `k % 2520` is 0), `p` is 2520, `s` is `k // 2520`, `d` is `k % 2520`, `A` is a 3x3 matrix of integers where each row is prepended with `0` and contains integers read from input, `B` is a 3x3 matrix of integers where each row is prepended with `0` and contains integers read from input, `j` is `k % 2520 - 1`, `i` is 2520.
    print(u + x * s, v + y * s)
#Overall this is what the function does:The function `func` reads input values for `k`, `a`, and `b`, and two 3x3 matrices `A` and `B`. It then simulates a game where Alice and Bob make choices based on their previous choices and the matrices `A` and `B`. The function calculates the number of times Alice and Bob choose options that satisfy a specific condition over `k` rounds. Specifically, it computes the total number of times Alice and Bob choose options such that `a - 1 == b % 3` and `b - 1 == a % 3`, respectively. The function prints the final counts of these occurrences. The function handles large values of `k` by breaking the simulation into segments of 2520 rounds, optimizing the computation. Edge cases include handling the initial values of `a` and `b` and ensuring the matrices `A` and `B` are correctly read and used in the calculations.

