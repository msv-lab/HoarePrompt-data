#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output state will consist of 'Bob' or 'Alice' printed for each iteration of the loop based on the condition `if (a + b) & 1 == 0`. The exact sequence of 'Bob' and 'Alice' depends on the input provided during each iteration of the loop.
#Overall this is what the function does:The function reads multiple pairs of non-negative integers \(a\) and \(b\) (where \(1 \leq a, b \leq 10^9\)) from the standard input. For each pair, it checks if their sum is even. If the sum is even, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return any value but prints 'Bob' or 'Alice' for each input pair.

