#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has executed all its iterations, with `t` equal to `test - 1`. The values of `a` and `b` are the last two integers input by the user during the loop's final iteration. If the sum of `a` and `b` is even, the output was 'Bob' for each iteration where the sum was even; otherwise, the output was 'Alice' for each iteration where the sum was odd.
#Overall this is what the function does:The function reads multiple pairs of non-negative integers (a and b) within the range of 1 to 10^9, checks if their sum is even or odd, and prints 'Bob' for each pair with an even sum and 'Alice' for each pair with an odd sum. After processing all input pairs, the function concludes without returning any value.

