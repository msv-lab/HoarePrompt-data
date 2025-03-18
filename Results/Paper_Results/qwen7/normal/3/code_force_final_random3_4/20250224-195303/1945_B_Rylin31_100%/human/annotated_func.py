#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The value of `t` remains an integer between 1 and \(10^4\), `i` is 9999 (since the loop runs from `i` in range(t) and `t` is at most \(10^4\)), and `a`, `b`, and `m` are integers obtained from the input split by spaces for the last iteration of the loop.
    #
    #This means that after all iterations of the loop have finished, `t` will still hold its initial value as it is not modified within the loop. The variable `i` will be equal to `t - 1` because the loop runs from `0` to `t-1`. The values of `a`, `b`, and `m` will be the ones provided by the input for the last iteration of the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates and prints the value of \(m // a + m // b + 2\). After processing all test cases, the function does not return any value but prints the calculated results for each test case.

