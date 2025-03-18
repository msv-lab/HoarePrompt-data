#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 1000, and for each i from 1 to t, n is an integer, a is a list of integers with leading and trailing zeros removed, and res is an integer representing the count of zeros in the modified list a.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` representing the number of cases, an integer `n` indicating the number of cells, and a list of `n` integers (0 or 1) indicating the presence of chips in the cells. It removes any leading and trailing zeros from the list and counts the remaining zeros. The function prints the count of zeros for each test case.

