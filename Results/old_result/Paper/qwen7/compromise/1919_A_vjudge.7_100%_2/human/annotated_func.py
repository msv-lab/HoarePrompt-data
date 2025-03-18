#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output state will consist of 'Bob' or 'Alice' printed based on the condition (a + b) & 1 == 0 for each iteration of the loop. The exact sequence of 'Bob' and 'Alice' depends on the input provided during each iteration.
#Overall this is what the function does:The function reads multiple pairs of non-negative integers \(a\) and \(b\) (where \(1 \leq a, b \leq 10^9\)) from the standard input, checks if their sum is even, and prints 'Bob' if the sum is even, otherwise prints 'Alice' for each pair. The function does not return any value but outputs the results directly to the standard output.

