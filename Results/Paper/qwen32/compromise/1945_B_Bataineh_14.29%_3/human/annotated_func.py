#State of the program right berfore the function call: Each test case consists of three positive integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a and b represent the frequencies of launching fireworks for the first and second installations, respectively, and m represents the duration (in minutes) that each firework is visible in the sky after launch. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: the sequence of printed results for each test case, which is either `2` or `m // a + m // b + 2` depending on the condition `m < a or m < b`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers `a`, `b`, and `m`. It calculates and prints the total number of minutes during which fireworks are visible in the sky for each test case. If the duration `m` is less than either `a` or `b`, it prints `2`. Otherwise, it prints the sum of the integer divisions of `m` by `a` and `m` by `b`, plus `2`.

