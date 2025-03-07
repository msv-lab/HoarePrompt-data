#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: For each test case, the loop will output the minimum length of consecutive segments of the same number in the array `ar`. If the array is uniform (all elements are the same) or if no such segment exists, it will output -1. The variables `t`, `n`, and `ar` will retain their initial values for the next test case, while `same`, `num`, `minn`, and `i` will be reset for each new test case.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `n` and a list `a` of `n` integers. For each test case, it outputs the minimum length of consecutive segments of the same number in the array `a`. If the array is uniform (all elements are the same) or if no such segment exists, it outputs -1. The function does not return any value; it only prints the results. The variables `t`, `n`, and `a` are read from input and retain their values for the next test case, while internal variables `same`, `num`, `minn`, and `i` are reset for each new test case.

