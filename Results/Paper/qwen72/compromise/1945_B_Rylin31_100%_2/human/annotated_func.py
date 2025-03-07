#State of the program right berfore the function call: The function should take three parameters a, b, and m, where a and b are the frequencies of launching fireworks for the first and second installations, respectively, and m is the visibility duration of each firework. All parameters are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers `a`, `b`, and `m` from the input, then print the value of `m // a + m // b + 2`. After all iterations, the values of `a`, `b`, and `m` will be undefined or reset to their initial input values for the next iteration, if any. The value of `t` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `a` and `b` are the frequencies of launching fireworks from two installations, and `m` is the visibility duration of each firework. The function then calculates and prints the value of `m // a + m // b + 2` for each test case. After all test cases are processed, the function completes without returning any value. The state of the program after the function concludes is that `t` remains unchanged, and the values of `a`, `b`, and `m` are undefined or reset for each iteration.

