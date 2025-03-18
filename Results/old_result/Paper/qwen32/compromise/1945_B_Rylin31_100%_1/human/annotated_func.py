#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) representing the frequency of launching fireworks for the first and second installations, and the visibility duration of each firework, respectively. The input starts with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases, followed by t lines, each containing the integers a, b, and m for a test case.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The output state consists of `t` lines, each line being the result of `m // a + m // b + 2` for the corresponding input values of `a`, `b`, and `m`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the value of `m // a + m // b + 2`. The function outputs one result per test case.

