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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: _ is t-1, n is an input integer, ar is a list of integers input by the user, same is 1, num is the last element of ar, i is equal to the length of ar, and minn is the minimum value of consecutive identical elements in ar. If minn is `inf` or equal to the length of `ar`, then minn is -1. Otherwise, minn is the smallest number of consecutive identical elements found in any of the arrays processed.
#Overall this is what the function does:The function processes multiple test cases, each with an integer `n` and a list of integers `a` of length `n`. It determines the minimum length of consecutive identical elements in the list `a` for each test case. If the list `a` is entirely composed of the same element or if no such consecutive identical elements are found, it prints `-1`. Otherwise, it prints the minimum length of consecutive identical elements found in the list. After processing all test cases, the function has no return value, but it prints the result for each test case.

