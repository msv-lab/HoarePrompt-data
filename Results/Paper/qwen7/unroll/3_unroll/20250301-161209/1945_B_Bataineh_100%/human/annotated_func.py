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
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions provided within the loop for each iteration where `i` ranges from 0 to `t-1`. For each iteration, the values of `a`, `b`, and `m` are taken as input, and depending on their relationships, one of four outputs is generated: 2, 2 + `m` // `b`, 2 + `m` // `a`, or `m` // `a` + `m` // `b` + 2. The sequence of these outputs will form the final state after all iterations.
#Overall this is what the function does:The function processes a series of test cases (up to 10^4 cases), where for each case, it takes three integers \(a\), \(b\), and \(m\) as inputs. Based on the relationships between these integers, it prints one of four possible outputs: 2, \(2 + \frac{m}{b}\), \(2 + \frac{m}{a}\), or \(\frac{m}{a} + \frac{m}{b} + 2\). After processing all test cases, it concludes without returning any value.

