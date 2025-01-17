#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if n == 1:
            e = a
        else:
            c = a * n
            d = b + (n - 2) * a
            e = min(c, d)
        
        print(e)
        
    #State of the program after the  for loop has been executed: `t` is 0, `n` is an input integer, `a` is an input integer, `b` is an input integer, `c` is not defined, `d` is not defined, `e` is not defined.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads three integers `n`, `a`, and `b`. If `n` is 1, it sets `e` to `a`. Otherwise, it calculates two values `c` and `d`, where `c` is `a * n` and `d` is `b + (n - 2) * a`, and then sets `e` to the minimum of `c` and `d`. After processing all test cases, it prints the value of `e` for each test case.

