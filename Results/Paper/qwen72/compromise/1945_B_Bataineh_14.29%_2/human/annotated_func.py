#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has finished executing all t iterations. For each iteration, the output is either 2 if m is less than a or b, or m // a + m // b + 2 otherwise. The values of t, a, b, and m are unchanged after each iteration, but the loop has processed t test cases.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then prints either `2` if `m` is less than `a` or `b`, or `m // a + m // b + 2` otherwise. After processing all `t` test cases, the function completes, and the state of the program is unchanged except for the output produced.

