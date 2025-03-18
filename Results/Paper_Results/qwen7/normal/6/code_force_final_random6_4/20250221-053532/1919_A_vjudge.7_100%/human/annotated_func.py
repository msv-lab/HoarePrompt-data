#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has completed all its iterations. The variable `test` is an input integer within the range 1 ≤ `test` ≤ 1000. The variable `t` is now equal to `test - 1`, meaning it has gone through all the iterations from 0 to `test - 1`. For each iteration, the values of `a` and `b` are the integers provided as input, and the if-else condition is evaluated. Depending on whether `a + b` is even or odd, either "Bob" or "Alice" is printed, but the values of `a` and `b` themselves do not change.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks if the sum of \(a\) and \(b\) is even or odd. If the sum is even, it prints "Bob"; otherwise, it prints "Alice". After processing all test cases, the function does not return any value but prints the results for each test case.

