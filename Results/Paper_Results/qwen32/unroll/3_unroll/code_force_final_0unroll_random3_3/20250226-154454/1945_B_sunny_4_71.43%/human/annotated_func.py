#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: For each of the `t` test cases, the program will output the sum of `A` and `B`, where `A` is calculated as `int(m / a) + 1` and `B` is calculated as `int(m / b) + 1`. The values of `t`, `a`, `b`, and `m` for each test case will remain unchanged after the loop execution.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads three positive integers `a`, `b`, and `m`. It then calculates and prints the sum of `A` and `B`, where `A` is `int(m / a) + 1` and `B` is `int(m / b) + 1`. The values of `t`, `a`, `b`, and `m` remain unchanged after processing each test case.

