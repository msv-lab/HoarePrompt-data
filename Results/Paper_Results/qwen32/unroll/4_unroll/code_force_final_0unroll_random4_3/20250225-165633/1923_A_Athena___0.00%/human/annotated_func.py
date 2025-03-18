#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (2 ≤ n ≤ 50) representing the number of cells, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 1), where a_i = 0 indicates that the i-th cell is free and a_i = 1 indicates that the i-th cell contains a chip. It is guaranteed that in each test case, there is at least one cell that contains a chip.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: the modified list `a` and the count `res` for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of cells where each cell is either free (0) or contains a chip (1). For each test case, it calculates and prints the number of free cells between the first and last chip in the list.

