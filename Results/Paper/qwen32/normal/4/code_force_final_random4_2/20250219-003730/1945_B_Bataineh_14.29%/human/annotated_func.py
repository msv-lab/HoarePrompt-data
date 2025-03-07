#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) representing the frequency of launching fireworks for the first and second installations, and the visibility duration of each firework, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ `t` ≤ 10^4; `i` is equal to `t` (the loop has completed all iterations); no further values of `a`, `b`, and `m` are read from the input as the loop has finished executing.
#Overall this is what the function does:The function processes `t` test cases, where for each test case it receives three integers `a`, `b`, and `m`. It calculates and prints the number of moments within the visibility duration `m` when both fireworks are visible, based on their launch frequencies `a` and `b`. If the visibility duration `m` is less than either `a` or `b`, it prints `2`. Otherwise, it prints the calculated number of moments.

