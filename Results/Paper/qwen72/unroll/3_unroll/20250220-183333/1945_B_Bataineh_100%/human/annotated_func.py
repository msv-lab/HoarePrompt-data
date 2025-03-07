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
        
    #State: The values of t, a, b, and m remain unchanged, but the loop has printed the results of the conditions for each of the t test cases.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 10^4`. For each of the `t` test cases, it reads three integers `a`, `b`, and `m` from the input, where `1 ≤ a, b, m ≤ 10^18`. It then prints a result based on the following conditions for each test case:
- If `m` is less than both `a` and `b`, it prints `2`.
- If `m` is less than `a` but greater than `b`, it prints `2 + m // b`.
- If `m` is less than `b` but greater than `a`, it prints `2 + m // a`.
- If `m` is greater than or equal to both `a` and `b`, it prints `m // a + m // b + 2`.

After the function concludes, the values of `t`, `a`, `b`, and `m` remain unchanged, and the results for each test case have been printed to the console.

