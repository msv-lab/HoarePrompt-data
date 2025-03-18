#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases (1 ≤ t ≤ 1000), and a list of lists, where each inner list represents a test case containing an integer n (2 ≤ n ≤ 50) and a list of n integers (0 ≤ a_i ≤ 1) indicating the state of each cell. Each test case must have at least one cell containing a chip (a_i = 1).
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
        
    #State: The variable `t` is unchanged, and for each test case, the variable `res` holds the number of zeros between the first and last occurrence of a chip (`1`) in the list `a`. The list `a` is modified to only contain the elements between the first and last chip, inclusive.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers (0 or 1) from the input. The function then processes each test case to count the number of zeros between the first and last occurrence of a chip (1) in the list. It prints this count for each test case. The function does not return any value. The variable `t` remains unchanged, and the list `a` is modified to only contain the elements between the first and last chip, inclusive, for each test case.

