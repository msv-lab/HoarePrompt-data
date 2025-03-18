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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of integers of length n where 1 ≤ a_i ≤ n, the array `a` is guaranteed to be beautiful, the sum of `n` over all test cases does not exceed 3 · 10^5, `ar` is a list of integers input by the user with at least 2 elements, `i` is `len(ar)`, `num` is the last integer in `ar`, `same` is the count of consecutive occurrences of the last integer in `ar`, and `minn` is the minimum length of any contiguous subarray of `ar` that consists of the same integer. If `minn` is `inf` or equal to `len(ar)`, then `minn` is updated to the value of `same`. Otherwise, `minn` is the minimum value between the original `minn` and `same`, and it is neither `inf` nor equal to `len(ar)`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` and a list `a` of integers of length `n`. For each test case, it calculates the minimum length of any contiguous subarray of `a` that consists of the same integer. If no such subarray exists or if the entire array consists of the same integer, it prints `-1`. Otherwise, it prints the minimum length found.

