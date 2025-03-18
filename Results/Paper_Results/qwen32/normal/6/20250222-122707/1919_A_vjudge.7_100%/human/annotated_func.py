#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer such that `t` is equal to `test` (i.e., the loop has finished all its iterations), `test` is an integer greater than or equal to 1 and less than or equal to 1000, `a` and `b` are integers provided by the input, and the sum of `a` and `b` is either even or odd. The loop has executed `test` times, and for each execution, it printed either 'Bob' or 'Alice' based on whether the sum of `a` and `b` was even or odd.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads two integers `a` and `b`. It then determines if the sum of `a` and `b` is even or odd, printing 'Bob' if the sum is even and 'Alice' if the sum is odd.

