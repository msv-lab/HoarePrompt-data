#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the time a firework is visible in the sky. The number of test cases, t, satisfies 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, where `t` is the initial input integer. For each iteration, the values of `a`, `b`, and `m` are read from the input, and the expression `m // a + m // b + 2` is computed and printed. The variable `i` has been incremented from 0 to `t-1` during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: `a`, `b`, and `m`. For each test case, it calculates and prints the number of moments in time when fireworks from both installations are visible in the sky.

