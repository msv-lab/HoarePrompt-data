#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state will consist of "Bob" printed for each iteration where the absolute difference between `a` and `b` is even, and "Alice" printed for each iteration where the absolute difference is odd. Since the initial state only defines `t` (an integer between 1 and 1000), the exact output cannot be determined without knowing the specific values of `a` and `b` for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks whether the absolute difference between \(a\) and \(b\) is even or odd. If the difference is even, it prints "Bob"; if the difference is odd, it prints "Alice". After processing all test cases, the function does not return any value but prints the results for each test case.

