#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: Output State: `t` is 0, `a` is an input integer, `b` is an input integer, `m` is an input integer, `A` is equal to `int(m / a) + 1`, `B` is equal to `int(m / b) + 1`.
    #
    #This means that after all the iterations of the loop have finished, the value of `t` has reached 0, indicating that there are no more inputs left to process. The values of `a`, `b`, and `m` from the last iteration are retained, and the calculations for `A` and `B` based on these values have been performed and printed.
#Overall this is what the function does:The function processes up to 10,000 test cases, where for each test case, it reads three integers \(a\), \(b\), and \(m\). It calculates two values, \(A\) and \(B\), where \(A\) is \(\left\lceil \frac{m}{a} \right\rceil + 1\) and \(B\) is \(\left\lceil \frac{m}{b} \right\rceil + 1\). For each test case, it prints the sum of \(A\) and \(B\). After processing all test cases, the function outputs nothing further, leaving the input variables in their final states from the last test case.

