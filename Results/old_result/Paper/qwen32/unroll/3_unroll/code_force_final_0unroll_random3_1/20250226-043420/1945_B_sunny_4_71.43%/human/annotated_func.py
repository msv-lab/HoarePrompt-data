#State of the program right berfore the function call: Each test case contains three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) representing the frequency of launching fireworks for the first and second installations, and the visibility duration of each firework, respectively. There are t (1 ≤ t ≤ 10^4) test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: A series of integers, each representing the sum of `A` and `B` for each test case, where `A = int(m / a) + 1` and `B = int(m / b) + 1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the sum of two values `A` and `B`, where `A` is the number of times fireworks from the first installation are visible within the duration `m` plus one, and `B` is the number of times fireworks from the second installation are visible within the duration `m` plus one.

