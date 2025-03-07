#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a and b represent the frequency of launching fireworks for the first and second installations, respectively, and m represents the duration for which each firework is visible in the sky. The input starts with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases, followed by t lines, each containing three integers a, b, and m for each test case.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: `t` is the same as the initial value, `a`, `b`, and `m` are the values from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. It calculates and prints the result based on the frequencies of launching fireworks (`a` and `b`) and the duration of visibility (`m`) for each test case.

