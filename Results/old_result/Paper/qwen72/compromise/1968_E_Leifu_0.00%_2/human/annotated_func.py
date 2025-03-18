#State of the program right berfore the function call: The function should accept an integer n (2 ≤ n ≤ 10^3) as input, and n is the size of the grid (n x n).
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
        
    #State: `n` is an input integer, `t` is 0, and `i` is `t - 1`. If `n` is 3, `j` is not modified. If `n` is greater than 3, `j` is set to `n`.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` (2 ≤ n ≤ 10^3) representing the size of an n x n grid. The function then prints a series of coordinates for each test case. Specifically, it always prints the coordinates (1, 1) and (1, 2). If `n` is 3, it prints (2, 3). If `n` is greater than 3, it prints (2, 4) and then prints (j, j) for all integers `j` from 4 to `n`. After processing all test cases, the function concludes.

