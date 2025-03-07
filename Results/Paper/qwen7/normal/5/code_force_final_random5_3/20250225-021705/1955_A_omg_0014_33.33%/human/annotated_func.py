#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an integer that was initially provided and must be greater than 0, i is equal to n - 1 (after all iterations of the loop), a, b, and c are integers obtained from the input split during each iteration, d is equal to c / 2 for each iteration, and the loop has printed either a * b or round(a * d) for each iteration based on the condition a * b < a * d.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers \(n\), \(a\), and \(b\). It calculates and prints either \(a \times b\) or \(a \times \frac{c}{2}\) (where \(c\) is another input integer) based on whether \(a \times b\) is less than \(a \times \frac{c}{2}\). After processing all test cases, the function does not return any value.

