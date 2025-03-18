#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is greater than 0 and less than or equal to 10^4, `i` is equal to `t-1`, `a`, `b`, and `m` are integers entered by the user for each iteration. The output consists of `t` lines, where each line contains either 2 or the value of `m // a + m // b + 2` based on the condition `m >= a` and `m >= b`.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it checks if \(m\) is at least as large as both \(a\) and \(b\). If \(m\) is smaller than either \(a\) or \(b\), it prints 2. Otherwise, it calculates and prints the value of \(m // a + m // b + 2\). The function reads these integers from standard input and outputs the results to standard output, producing a total of up to 10,000 lines of output.

