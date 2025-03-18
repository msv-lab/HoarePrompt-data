#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
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
        
    #State: `i` is equal to `t`, and no other variables (`a`, `b`, `m`) retain specific values as they are re-assigned in each iteration.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads three positive integers `a`, `b`, and `m`. It then calculates and prints a value based on the conditions involving `a`, `b`, and `m`. Specifically, it prints `2` if both `a` and `b` are greater than `m`. If only `b` is greater than `m`, it prints `2 + m // b`. If only `a` is greater than `m`, it prints `2 + m // a`. Otherwise, it prints `m // a + m // b + 2`. The function does not return any value; it only prints the result for each test case.

