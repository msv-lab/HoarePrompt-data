#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The value of `t` must be greater than or equal to the total number of iterations the loop will run, `i` will be equal to `t`, `a` will be the last input integer received for the first iteration, `b` will be the last input integer received for the second iteration, and `m` will be the last input integer received for the third iteration. The loop will print the result of the expression `m // a + m // b + 2` for each iteration from 0 to `t-1`.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` will be the final value it was initialized to, `i` will be equal to `t`, and `a`, `b`, and `m` will hold the values of the last set of inputs provided for the last iteration of the loop. The loop will have printed the result of the expression `m // a + m // b + 2` for each of the `t` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)), and prints the result of the expression \(m // a + m // b + 2\) for each test case. After processing all test cases, the function does not return any value.

