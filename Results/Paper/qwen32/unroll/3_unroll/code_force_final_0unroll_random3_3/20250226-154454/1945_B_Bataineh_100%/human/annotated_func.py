#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
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
        
    #State: A series of printed values based on the logic: for each test case, if `m < a` and `m < b`, print `2`; if `m < a` and `m > b`, print `2 + m // b`; if `m < b` and `m > a`, print `2 + m // a`; otherwise, print `m // a + m // b + 2`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then prints a calculated value based on the conditions: if `m` is less than both `a` and `b`, it prints `2`; if `m` is less than `a` but greater than `b`, it prints `2 + m // b`; if `m` is less than `b` but greater than `a`, it prints `2 + m // a`; otherwise, it prints `m // a + m // b + 2`.

