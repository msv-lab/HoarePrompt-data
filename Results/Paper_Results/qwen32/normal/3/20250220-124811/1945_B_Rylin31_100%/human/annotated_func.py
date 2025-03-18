#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a and b represent the frequency of launching fireworks for the first and second installations, respectively, and m represents the duration for which each firework is visible in the sky. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, where `t` is the initial input integer. For each of the `t` iterations, the loop reads three integers `a`, `b`, and `m` from the input, and prints the result of `m // a + m // b + 2`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the value of `m // a + m // b + 2`.

