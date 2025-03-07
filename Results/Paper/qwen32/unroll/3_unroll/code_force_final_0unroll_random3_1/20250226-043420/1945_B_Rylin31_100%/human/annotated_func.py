#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the function receives three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the duration for which each firework is visible in the sky after launch.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: For each test case, the number of times fireworks are visible in the sky, calculated as (m // a) + (m // b) + 2, is printed. The variable `t` remains unchanged and represents the number of test cases processed.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `a`, `b`, and `m`. It calculates and prints the total number of distinct moments during the duration `m` when at least one firework is visible in the sky, based on the launch frequencies `a` and `b` for two different installations.

