#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10000, and for each of the t test cases, a and b are integers where 0 ≤ a, b ≤ 10^6.
def func():
    t = int(raw_input())
    for i in range(0, t):
        a, b = map(int, raw_input().split())
        
        if b == 0:
            print(1)
            continue
        
        if a == 0:
            print(0.5)
            continue
        
        p = a * b + max(a - 4 * b, 0) * b
        
        q = a * 2 * b
        
        a = min(a, 4 * b)
        
        p = p + a * a / 8.0
        
        print(p / (1.0 * q))
        
    #State of the program after the  for loop has been executed: `t` is an integer input by the user where \(1 \leq t \leq 10000\), `i` is `t - 1`, `a` and `b` are the values read from the user during the last iteration, `p` is `a * b + max(a - 4 * b, 0) * b + a * a / 8.0`, `q` is `a * 2 * b`, and the loop has printed a value for each of the `t` test cases, either 1, 0.5, or the result of `p / (1.0 * q)`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where `1 ≤ t ≤ 10000`. For each test case, it reads two integers `a` and `b` (where `0 ≤ a, b ≤ 10^6`). The function then computes and prints a result for each test case based on the following rules:
- If `b` is 0, it prints 1.
- If `a` is 0, it prints 0.5.
- Otherwise, it calculates `p` as `a * b + max(a - 4 * b, 0) * b + (min(a, 4 * b)

