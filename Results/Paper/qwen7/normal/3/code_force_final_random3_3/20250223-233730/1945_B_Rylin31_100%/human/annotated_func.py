#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The value of `t` must be an integer between 1 and \(10^4\), `i` will be equal to the final value of `t-1` after the loop completes, `a`, `b`, and `m` will each be the last set of integers entered by the user for their respective iteration of the loop. The loop will have processed `t` iterations, with each iteration reading three integers (`a`, `b`, `m`) from the user input and printing the result of `m // a + m // b + 2`.
#Overall this is what the function does:The function processes up to 10,000 test cases, where for each test case, it reads three integers \(a\), \(b\), and \(m\) (each between 1 and \(10^{18}\)). For each set of inputs, it calculates and prints the value of \(m // a + m // b + 2\). After processing all test cases, the function concludes with no return value.

