#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: Output State: `t` is 0, `n` remains as the original input integer, `i` is equal to `n`.
    #
    #In Natural Language: After the loop has executed all its iterations, the variable `t` will be 0 because it is decremented by `n` after each full iteration of the loop, and `n` is the number of iterations. The variable `n` remains as the original input integer because it is not modified within the loop. The variable `i` will be equal to `n`, as the loop increments `i` from 1 to `n` inclusive, and the last value `i` takes is `n`.
#Overall this is what the function does:The function processes a series of test cases defined by the variable `t`. For each test case, it reads an integer `n` and prints a line containing `n` occurrences of '1' followed by the integers from 1 to `n`. After processing all test cases, the variable `t` is set to 0, `n` retains its original value from the last test case, and `i` is equal to `n`.

