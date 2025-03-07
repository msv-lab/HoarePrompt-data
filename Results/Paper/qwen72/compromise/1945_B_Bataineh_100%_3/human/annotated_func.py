#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
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
        
    #State: The values of t, a, b, and m remain unchanged, but the loop has printed a series of integers based on the conditions evaluated for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `t` represents the number of test cases, and for each test case, it reads three integers `a`, `b`, and `m` from the input. It then evaluates a series of conditions based on the values of `a`, `b`, and `m` and prints an integer result for each test case. The final state of the program is that the input values `t`, `a`, `b`, and `m` remain unchanged, but the function has printed a series of integers, one for each test case.

