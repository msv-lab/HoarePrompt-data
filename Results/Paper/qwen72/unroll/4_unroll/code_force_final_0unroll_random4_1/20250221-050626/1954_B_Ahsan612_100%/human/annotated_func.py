#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of integers of length n where 1 ≤ a_i ≤ n. Additionally, in every test case, the array a is beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates over each test case, and for each test case, it processes the list `ar` to find the minimum length of consecutive segments of the same number that are not the entire list. If no such segment exists or the entire list is a single segment, it prints `-1`. Otherwise, it prints the minimum segment length. The variables `t`, `n`, and `a` remain unchanged, while the loop variables `same`, `num`, `minn`, and `i` are reset or updated for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `t`, an integer `n`, and a list of integers `a` of length `n`. For each test case, it reads `n` and the list `a` from the input, then finds the minimum length of consecutive segments of the same number in `a` that are not the entire list. If no such segment exists or the entire list is a single segment, it prints `-1`. Otherwise, it prints the minimum segment length. The function does not return any value; it only prints the results. The input variables `t`, `n`, and `a` remain unchanged after the function execution.

