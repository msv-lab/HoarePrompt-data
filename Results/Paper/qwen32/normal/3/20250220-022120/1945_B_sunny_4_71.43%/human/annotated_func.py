#State of the program right berfore the function call: Each test case consists of three integers a, b, m (1 ≤ a, b, m ≤ 10^18) representing the frequency of launching fireworks for the first and second installations, and the duration for which each firework is visible in the sky. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The loop will have executed `t` times, with each iteration calculating and printing `A + B` where `A` is `int(m / a) + 1` and `B` is `int(m / b) + 1` based on the input values of `a`, `b`, and `m` provided for that iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the sum of `int(m / a) + 1` and `int(m / b) + 1`.

