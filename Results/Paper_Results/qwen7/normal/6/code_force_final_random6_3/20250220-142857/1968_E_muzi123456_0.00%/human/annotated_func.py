#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: Output State: `t` is 0, `n` is an integer between 2 and 10^3, inclusive, `i` is equal to `n`.
    #
    #Explanation: After the loop executes all its iterations, `t` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The variable `n` retains its original input integer value as it is only assigned a new value inside the loop but does not get decremented or modified otherwise. The variable `i` will be equal to `n` because the loop increments `i` from 1 to `n` inclusive, and after all iterations, `i` will reach `n`.
#Overall this is what the function does:The function processes a series of test cases defined by the integer `t`. For each test case, it reads an integer `n` and prints a line containing `n` occurrences of '1' followed by the numbers from 1 to `n`, each separated by a space. After processing all test cases, the function ensures that `t` is set to 0.

