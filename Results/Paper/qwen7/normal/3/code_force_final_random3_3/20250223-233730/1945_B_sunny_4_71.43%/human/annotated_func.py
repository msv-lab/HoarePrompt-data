#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: t is an input integer between 0 and \(10^4 - 3\), `a`, `b`, and `m` are integers obtained from the input split and converted to integers, `A` is `int(m / a) + 1`, `B` is `int(m / b) + 1`, `A` is recalculated as `int(m / a) + 1` for each iteration.
#Overall this is what the function does:The function processes a series of test cases (up to 10,000). For each test case, it reads three integers \(a\), \(b\), and \(m\) and calculates two values \(A\) and \(B\) based on these inputs. Specifically, \(A\) is set to \(\text{int}(m / a) + 1\) and \(B\) is set to \(\text{int}(m / b) + 1\). The function then prints the sum \(A + B\) for each test case. After processing all test cases, the function concludes without returning any value.

