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
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 10^4, `i` is `t-1`, `a`, `b`, and `m` are new input integers for the last iteration. If `m` is less than both `a` and `b`, then `m` is less than both `a` and `b`. If `m` is between `a` and `b`, then `m` remains between `a` and `b`. Otherwise, `m` is either less than or equal to `a` or greater than or equal to `b`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, it reads three integers `a`, `b`, and `m` (1 ≤ a, b, m ≤ 10^18). It then prints a result based on the following conditions for each test case:
- If `m` is less than both `a` and `b`, it prints 2.
- If `m` is less than `a` and greater than `b`, it prints 2 plus the integer division of `m` by `b`.
- If `m` is less than `b` and greater than `a`, it prints 2 plus the integer division of `m` by `a`.
- Otherwise, it prints the sum of the integer divisions of `m` by `a` and `m` by `b`, plus 2. 

After the function concludes, `t` test cases have been processed, and the results for each test case have been printed to the console. The final state of the program is that all test cases have been evaluated and their respective results have been output.

