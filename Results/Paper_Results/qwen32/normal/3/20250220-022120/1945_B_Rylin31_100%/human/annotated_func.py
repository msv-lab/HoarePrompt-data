#State of the program right berfore the function call: Each test case consists of three integers a, b, and m where 1 ≤ a, b, m ≤ 10^18. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, and for each iteration, it has read three integers `a`, `b`, and `m` from the input, calculated the value `m // a + m // b + 2`, and printed this value. The variable `i` will be equal to `t` after the loop completes.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it computes the value `m // a + m // b + 2` and prints the result.

