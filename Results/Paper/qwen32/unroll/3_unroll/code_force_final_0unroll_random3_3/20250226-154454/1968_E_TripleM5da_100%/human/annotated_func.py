#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 50) representing the number of test cases. Each of the following t lines contains a single integer n (2 ≤ n ≤ 10^3) representing the size of the n x n grid for each test case.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: For each test case with size `n`, the output consists of the lines `1 1`, `1 2`, and `(i, i)` for each `i` from `3` to `n`.
#Overall this is what the function does:The function processes a series of test cases, where each test case is defined by an integer `n` representing the size of an `n x n` grid. For each test case, it outputs the coordinates `1 1`, `1 2`, and `(i, i)` for each `i` from `3` to `n`.

