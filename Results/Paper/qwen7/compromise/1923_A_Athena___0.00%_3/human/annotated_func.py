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
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: Output State: After the loop executes all iterations, `t` is 0, `res` is the total number of leading zeros in all the input lists `a` across all iterations, `i` is the index of the last remaining element in the list `a` from the last iteration (or -1 if the list is empty), and `len(a)` is the length of the list `a` with all leading zeros removed from the last iteration.
    #
    #This means that after all iterations of the loop have completed, the variable `t` which initially was set to an integer between 1 and 1000 will be reduced to 0 as each iteration decrements `t`. The variable `res` accumulates the count of leading zeros from all the lists `a` provided as inputs. The variables `i` and `len(a)` reflect the state of the last list processed after all leading zeros have been removed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (number of cells), and a list of `n` integers indicating whether each cell is free (0) or contains a chip (1). For each test case, it removes leading zeros from the list, counts the remaining leading zeros across all test cases, and prints the final list after removing leading zeros. The function then prints the total count of leading zeros removed from all test cases.

