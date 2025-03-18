#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
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
        
    #State: `t` is the user input, `i` is `t-1`, and `a`, `b`, and `m` are integers provided by the user for each iteration. For each iteration, if `m` is less than both `a` and `b`, the condition `m < a` and `m < b` is true. Otherwise, if `m` is less than `a` and greater than `b`, the condition `m < a and m > b` is true. If `m` is between `a` and `b` (i.e., `m < b and m > a`), the condition `m < b and m > a` is true. In all other cases, `m` is either less than or equal to `a` or greater than or equal to `b`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the user. It then prints a result for each test case based on the following conditions: 
- If `m` is less than both `a` and `b`, it prints `2`.
- If `m` is less than `a` and greater than or equal to `b`, it prints `2 + m // b`.
- If `m` is less than `b` and greater than or equal to `a`, it prints `2 + m // a`.
- In all other cases, it prints `m // a + m // b + 2`. 
The function does not return any value; it only prints the results for each test case.

