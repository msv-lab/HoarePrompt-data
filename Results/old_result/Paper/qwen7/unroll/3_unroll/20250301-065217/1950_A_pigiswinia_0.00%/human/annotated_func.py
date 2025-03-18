#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of `t` lines, each containing either 'STAIRS', 'PEAK', or 'NONE' based on the conditions evaluated for each set of inputs (a, b, c) provided by the user. The value of `t` is determined by the user's initial input, which specifies how many times the loop will run. Each line corresponds to the result of one iteration of the loop, depending on whether `a < b < c`, `a < b > c`, or neither condition is met.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer provided by the user and ranges from 1 to 1000. For each test case, it reads three integers `a`, `b`, and `c` (each ranging from 0 to 9). Based on the values of `a`, `b`, and `c`, it prints one of three strings: 'STAIRS', 'PEAK', or 'NONE'. After processing all `t` test cases, the function concludes without returning any value.

