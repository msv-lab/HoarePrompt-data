#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    """t=int(input())
    for _ in range(t):
        a,b,m=map(int,input().split())
        A=int(m/a)+1
        B=int(m/b)+1
        print(A+B)"""
    t = int(input())
    for qi in range(t):
        a, b, m = [int(x) for x in input().split()]
        
        ans = m // a + m // b + 2
        
        print(ans)
        
    #State: For each test case, the output is the sum of the integer division of m by a, the integer division of m by b, and 2. The loop iterates t times, and for each iteration, the values of a, b, and m are read from input, and the result is printed. After all iterations, the values of t, a, b, and m remain unchanged, but the output for each test case is printed.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases, where `1 ≤ t ≤ 10^4`. For each test case, it reads three integers `a`, `b`, and `m`, where `1 ≤ a, b, m ≤ 10^18`. It then calculates the sum of the integer division of `m` by `a`, the integer division of `m` by `b`, and 2. This result is printed for each test case. After processing all test cases, the function does not return any value, but the final state includes the printed output for each test case, and the input variables `t`, `a`, `b`, and `m` are not retained in the function's scope.

