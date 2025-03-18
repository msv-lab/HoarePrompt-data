#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `i` is equal to `n`, `n` must be greater than 0, `a`, `b`, and `c` are integers obtained from the input split by spaces for each iteration, `d` is equal to `c / 2` for each iteration, and the program prints either `a * b` or `round(a * d)` based on the if condition for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, a, and b. For each test case, it calculates either \(a \times b\) or \(round(a \times \frac{c}{2})\), where \(c\) is another integer input. It then prints the result for each test case. The function does not return any value but prints the results directly.

