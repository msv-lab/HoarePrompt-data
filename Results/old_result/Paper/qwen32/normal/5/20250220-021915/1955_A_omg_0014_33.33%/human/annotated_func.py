#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the following t lines contains three integers n, a, and b such that 1 ≤ n ≤ 100, 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: `t` is an integer such that 1 ≤ `t` ≤ 10^4; `n` is an integer; `i` is equal to `n` (indicating the loop has finished); `a`, `b`, and `c` are the last set of integers provided by the input; `d` is `c / 2`; the loop has printed `n` values, each being either `a * b` or `round(a * d)` based on the comparison condition.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints either `a * b` or `round(a * (c / 2))`, depending on whether `a * b` is less than `a * (c / 2)`. After processing all test cases, the function concludes without returning any value, as its output is through print statements.

