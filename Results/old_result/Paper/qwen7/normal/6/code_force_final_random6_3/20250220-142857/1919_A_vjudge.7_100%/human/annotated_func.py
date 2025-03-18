#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: After all iterations of the loop have finished, `test` must be equal to the total number of iterations, `t` will be `test`, `a` and `b` will be the last input integers split from the final input provided within the loop, and the loop has printed 'Bob' if `a + b` is even and 'Alice' if `a + b` is odd for each iteration based on the given inputs.
#Overall this is what the function does:The function reads multiple pairs of non-negative integers \(a\) and \(b\) (where \(1 \leq a, b \leq 10^9\)) from the user, checks if their sum is even or odd, and prints 'Bob' if the sum is even, and 'Alice' if the sum is odd for each pair. After processing all input pairs, it returns nothing.

