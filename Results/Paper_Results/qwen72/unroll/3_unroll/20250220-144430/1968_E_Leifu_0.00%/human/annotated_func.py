#State of the program right berfore the function call: The function should accept an integer n as input where 2 <= n <= 10^3, and n represents the size of the grid (n x n) and the number of cells to choose.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will print '1 1', '1 2', and then either '2 3' if `n` is 3, or '2 4' followed by a sequence of numbers from 4 to `n` inclusive, where each number is printed as 'j j'. The value of `n` will be updated based on the input provided for each iteration, and `t` will be decremented by 1 for each iteration until it reaches 0.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` (where 2 <= n <= 10^3) representing the size of an n x n grid. The function then prints a series of coordinates for each test case. Specifically, it prints '1 1', '1 2', and if `n` is 3, it prints '2 3'. Otherwise, it prints '2 4' followed by a sequence of coordinates from '4 4' to 'n n'. The function performs these actions for each of the `t` test cases.

