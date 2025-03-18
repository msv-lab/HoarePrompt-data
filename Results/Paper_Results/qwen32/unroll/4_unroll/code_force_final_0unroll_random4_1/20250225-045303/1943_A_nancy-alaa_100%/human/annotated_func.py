#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 2 * 10^4. For each test case, n is a positive integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies 0 <= a_i < n. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: For each test case, the smallest non-negative integer that is either not present in the list `a` or appears exactly once in the list `a` after the first occurrence of any integer that appears exactly once will be printed. The variable `t` remains unchanged, and the variables `n`, `arr`, and `mpp` will not retain their values after each iteration as they are reinitialized in each loop iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it prints the smallest non-negative integer that is either not present in the list `a` or appears exactly once in the list `a` after the first occurrence of any integer that appears exactly once.

