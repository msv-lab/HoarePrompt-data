#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: After the loop executes all iterations, `t` is greater than 0, `i` equals `t`, and `a` and `b` are integers from the input for each iteration, with their absolute difference being either even or odd as determined by the if-else block.
#Overall this is what the function does:The function reads multiple pairs of non-negative integers \(a\) and \(b\) (where \(1 \leq a, b \leq 10^9\)) from the user, checks if the absolute difference between \(a\) and \(b\) is even or odd, and prints "Bob" if the difference is even, otherwise prints "Alice". The function does not return any value.

