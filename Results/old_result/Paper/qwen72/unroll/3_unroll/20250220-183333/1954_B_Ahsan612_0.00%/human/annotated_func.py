#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of integers of length n where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: The variable `minn` is the minimum length of consecutive elements that are the same in the list `ar` for each test case. If all elements in `ar` are different, `minn` will be 1. If the list `ar` is empty or no consecutive elements are the same, `minn` will be -1. The variables `t`, `n`, and `ar` will retain their initial values for the next test case, and `i`, `same`, and `num` will be reset to their initial values for each new test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `ar` of `n` integers. It then calculates the minimum length of consecutive elements that are the same in the list `ar`. If all elements in `ar` are different, it prints 1. If the list `ar` is empty or no consecutive elements are the same, it prints -1. The function does not return any value but prints the result for each test case. The variables `t`, `n`, and `ar` retain their values for the next test case, while `i`, `same`, and `num` are reset for each new test case.

