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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, and for each input, the value of `res` is the count of zeros in the list `a` after removing leading and trailing zeros.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (1 ≤ t ≤ 1000), an integer `n` (2 ≤ n ≤ 50), and a list of `n` integers indicating whether cells contain chips (1) or are free (0). It removes any leading and trailing zeros from the list and counts the remaining zeros. Finally, it prints the count of zeros for each test case.

