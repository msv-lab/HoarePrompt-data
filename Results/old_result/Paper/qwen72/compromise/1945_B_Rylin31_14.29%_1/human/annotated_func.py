#State of the program right berfore the function call: The function should accept three parameters a, b, and m, where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the duration for which each firework is visible. All parameters are integers within the range 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The values of `a`, `b`, and `m` are not retained between iterations, and `t` remains unchanged. For each iteration, the loop reads new values for `a`, `b`, and `m` from input and prints the result of the computation based on these values. After `t` iterations, the loop finishes, and `t` is still the same as in the initial state.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from input, representing the frequencies of launching fireworks for two installations and the visibility duration of each firework, respectively. The function then calculates and prints the total number of distinct moments within the first `m` seconds when at least one firework is visible from either installation. After processing all `t` test cases, the function concludes, and the value of `t` remains unchanged. The function does not return any value.

