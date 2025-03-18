#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of t lists, where each inner list contains two elements: an integer n (2 ≤ n ≤ 50) representing the number of cells, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 1) representing the state of each cell (0 for free, 1 for a chip). Additionally, each test case must have at least one cell containing a chip.
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
        
    #State: t remains unchanged, and for each test case, the list `a` is trimmed to remove leading and trailing zeros, and the number of zeros in the trimmed list is printed.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 50) and a list of `n` integers (0 ≤ a_i ≤ 1) representing the state of each cell. The function trims the list to remove leading and trailing zeros, then prints the trimmed list. It also calculates and prints the number of zeros in the trimmed list. The function does not return any value. After the function concludes, `t` remains unchanged, and the input lists for each test case are modified by removing leading and trailing zeros.

