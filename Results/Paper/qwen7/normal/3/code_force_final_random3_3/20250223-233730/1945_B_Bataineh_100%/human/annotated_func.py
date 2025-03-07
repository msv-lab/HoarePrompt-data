#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: After the loop executes all iterations, `i` is equal to `t - 1`, `t` remains an integer between 1 and \(10^4\), and `a`, `b`, and `m` are integers assigned the values from the last iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates and prints a specific value based on the relationships between \(a\), \(b\), and \(m\). After processing all test cases, it returns nothing (void).

