#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of a series of lines, each containing either '2' or the result of the expression `m // a + m // b + 2`. The number of lines will be equal to the value of `t`, which was initially input by the user. Each line corresponds to one iteration of the loop, where `a`, `b`, and `m` are read from the input for that iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`, and calculates either `2` or the value of `m // a + m // b + 2` based on whether `m` is less than both `a` and `b`. It then prints the result for each test case. The function does not return any value but produces a series of outputs corresponding to each test case.

