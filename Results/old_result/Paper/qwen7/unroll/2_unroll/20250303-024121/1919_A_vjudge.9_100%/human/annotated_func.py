#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state will consist of a series of lines, each containing either "Bob" or "Alice", depending on the input pairs (a, b) provided for each iteration of the loop. Specifically, "Bob" will be printed if the absolute difference between a and b is even, and "Alice" will be printed if the absolute difference is odd. The number of lines will be equal to the value of t, which is the input integer between 1 and 1000.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: `t`, `a`, and `b`. It reads these integers from standard input, where `t` specifies the number of test cases. For each test case, the function compares the absolute difference between `a` and `b`. If the difference is even, it prints "Bob"; otherwise, it prints "Alice". After processing all test cases, the function concludes with no explicit return value but outputs a series of "Bob" or "Alice" based on the conditions specified.

