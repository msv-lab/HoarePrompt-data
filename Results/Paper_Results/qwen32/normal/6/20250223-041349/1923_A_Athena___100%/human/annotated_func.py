#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, there are two lines: the first line contains an integer n (2 ≤ n ≤ 50) representing the number of cells, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. It is guaranteed that in each test case, at least one cell contains a chip.
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
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is an integer representing the number of test cases and is 0; `n` is undefined as there are no more test cases to process; `a` is undefined as there are no more test cases to process; `res` is undefined as there are no more test cases to process.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of cells where each cell is either free (0) or contains a chip (1). For each test case, it calculates and prints the number of free cells between the first and last cell that contains a chip.

