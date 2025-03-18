#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case is defined by an integer `n` (2 ≤ n ≤ 10^3). The function should internally manage the input and output, ensuring that for each test case, it outputs `n` points that maximize the size of the set \(\mathcal{H}\) of distinct Manhattan distances between any pair of cells.
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
        
    #State: The loop will execute `t` times, where `t` is the number of test cases. For each test case, the loop will print '1 1', '1 2', and if `n` is 3, it will print '2 3'. Otherwise, it will print '2 4' and then for each integer `j` from 4 to `n` (inclusive), it will print `j j`. The variable `t` will remain unchanged, and the variable `n` will be the last input integer read for the final test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 10^3) and prints `n` points in a coordinate system. The points are printed in such a way that they maximize the set of distinct Manhattan distances between any pair of points. Specifically, it always prints the points (1, 1) and (1, 2). If `n` is 3, it prints the point (2, 3). Otherwise, it prints the point (2, 4) and then prints points (j, j) for each integer `j` from 4 to `n` (inclusive). The function does not return any value. The variable `t` remains unchanged, and `n` will be the last input integer read for the final test case.

