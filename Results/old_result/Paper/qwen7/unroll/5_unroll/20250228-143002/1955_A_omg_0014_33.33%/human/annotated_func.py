#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: Output State: The output state will consist of a series of lines, each containing either the value of `a * b` or the rounded value of `a * d`, depending on whether `a * b` is less than `a * d`. The number of lines will be equal to the value of `n`. Each line's specific value depends on the input provided for each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( a \), and \( b \). For each test case, it calculates either \( a \times b \) or the rounded value of \( a \times \frac{c}{2} \), where \( c \) is derived from the input. It then prints the result for each test case. The final state of the program consists of a series of outputs, each representing the calculated value for the respective test case.

