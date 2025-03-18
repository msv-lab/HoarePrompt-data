#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (2 ≤ n ≤ 50) representing the number of cells, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 1), where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. It is guaranteed that in each test case, there is at least one cell containing a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The loop has completed all `t` iterations. For each iteration, `n` is the input integer, `arr` is the input string, `x` is the index of the first occurrence of '1' in `arr` or -1 if '1' is not found, `y` is the index of the first occurrence of '1' in the reversed `arr` or -1 if '1' is not found, and `z` is the substring of `arr` from index `x` to `n - y`. The number of '0's in `z` is printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of cells, some of which contain chips (represented by 1) and some of which are free (represented by 0). For each test case, the function calculates and prints the number of free cells between the first and last chip in the list.

