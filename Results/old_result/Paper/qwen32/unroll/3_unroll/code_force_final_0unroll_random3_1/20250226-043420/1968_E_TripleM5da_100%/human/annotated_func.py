#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 50) representing the number of test cases. Each of the following t lines contains a single integer n (2 ≤ n ≤ 10^3) representing the size of the grid and the number of cells to choose.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: For each test case with input integer `n`, the output will be `1, 1`, `1, 2`, and then `i, i` for each `i` from `3` to `n`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it outputs a series of coordinate pairs starting with `(1, 1)` and `(1, 2)`, followed by `(i, i)` for each integer `i` from `3` to `n`.

