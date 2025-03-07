#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all i, and the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: After running the loop for `t` iterations, the output will consist of "Bob" or "Alice" printed for each iteration based on whether the number 1 is present in the list `l`. If 1 is found in any list `l`, "Bob" is printed; otherwise, "Alice" is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) indicating the number of test cases, followed by \( t \) groups of data. For each group, it reads a positive integer \( n \) and a list of \( n \) integers. It checks if the number 1 is present in the list. If 1 is found in any list, it prints 'Bob'; otherwise, it prints 'Alice' for each test case. The function does not return any value but prints the result for each test case.

