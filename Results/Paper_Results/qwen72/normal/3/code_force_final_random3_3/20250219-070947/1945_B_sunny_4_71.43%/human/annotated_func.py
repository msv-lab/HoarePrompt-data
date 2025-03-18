#State of the program right berfore the function call: The function should accept three parameters a, b, and m, where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the visibility duration of each firework. All parameters are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: `a`, `b`, and `m` are assigned new integer values from the input, `t` is equal to the number of iterations, `_` is `t - 1`, `A` is equal to `int(m / a) + 1`, `B` is equal to `int(m / b) + 1`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `a` and `b` are the frequencies of launching fireworks for two installations, and `m` is the visibility duration of each firework. It calculates the total number of distinct moments when at least one firework is visible by computing `A = int(m / a) + 1` and `B = int(m / b) + 1`, and then prints the sum `A + B`. The function does not return any value; it only prints the result for each test case.

