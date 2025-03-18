#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: The loop has completed all its iterations, with `t` being the initial input integer between 1 and 10^4, `i` equal to `t`, and `a`, `b`, and `m` holding the last set of input integers processed within the loop. The value of `t` remains unchanged throughout the loop's execution, and `i` increments by 1 in each iteration until it reaches `t`. The values of `a`, `b`, and `m` are updated based on the input provided in each iteration but retain the final values from the last iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a value based on the relationships between `a`, `b`, and `m`. If `m` is less than both `a` and `b`, it prints `2`. If `m` is less than one but not the other, it prints either `2 + m // b` or `2 + m // a`. Otherwise, it prints `m // a + m // b + 2`. After processing all test cases, the function does not return any value but prints the calculated values for each test case.

