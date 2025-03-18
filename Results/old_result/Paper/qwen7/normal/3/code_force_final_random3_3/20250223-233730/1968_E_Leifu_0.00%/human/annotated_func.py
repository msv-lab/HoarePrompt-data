#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: Output State: After the loop executes all its iterations, `t` must be greater than 0 and less than or equal to 50, `n` must be greater than or equal to 10, `i` will be equal to `t-1`, and `j` will be equal to `n`.
    #
    #This means that after the loop has completed all its iterations, the variable `t` (which represents the number of times the outer loop runs) will be decremented by 1 with each iteration until it reaches 0. The variable `n` will be set to at least 10 based on the condition within the loop. The variable `i` will hold the value of `t-1` as it gets updated after each iteration of the outer loop. The variable `j` will be equal to `n` because it is set inside the inner loop which runs from 4 to `n`, and since `n` is at least 10, `j` will also be 10 or greater.
#Overall this is what the function does:The function processes a series of test cases defined by the integer `t`. For each test case, it reads an integer `n`. It then prints a sequence of pairs of integers. Specifically, it always prints '1 1' and '1 2'. If `n` is 3, it prints '2 3'; otherwise, it prints '2 4' followed by pairs of integers from 4 to `n`. After processing all test cases, the function does not return any value.

