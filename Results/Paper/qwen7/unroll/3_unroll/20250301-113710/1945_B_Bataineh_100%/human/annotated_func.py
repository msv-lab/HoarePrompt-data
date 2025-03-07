#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: Output State: The output state will consist of a series of integers printed as a result of the loop executing `t` times. For each iteration, the value printed depends on the comparison between `m`, `a`, and `b`. Specifically:
    #
    #- If `m` is less than both `a` and `b`, it prints `2`.
    #- If `m` is less than `a` but greater than `b`, it prints `2 + m // b`.
    #- If `m` is less than `b` but greater than `a`, it prints `2 + m // a`.
    #- Otherwise, it prints `m // a + m // b + 2`.
    #
    #Each line of the output corresponds to one iteration of the loop, with `i` ranging from `0` to `t-1`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of four integers: t, a, b, and m. It verifies that t is within the range 1 to 10^4 and that a, b, and m are within the range 1 to 10^18. For each test case, it prints an integer based on the comparison between m, a, and b. Specifically, it prints 2 if m is less than both a and b, 2 + m // b if m is less than a but greater than b, 2 + m // a if m is less than b but greater than a, and m // a + m // b + 2 otherwise.

