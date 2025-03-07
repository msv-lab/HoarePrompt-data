#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the time each firework is visible in the sky. The number of test cases, t, satisfies 1 ≤ t ≤ 10^4.
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
        
    #State: `t` remains unchanged, `a`, `b`, and `m` hold the values assigned during the last iteration of the loop, and `i` equals `t`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the number of moments in time when fireworks from both installations are visible in the sky simultaneously.

