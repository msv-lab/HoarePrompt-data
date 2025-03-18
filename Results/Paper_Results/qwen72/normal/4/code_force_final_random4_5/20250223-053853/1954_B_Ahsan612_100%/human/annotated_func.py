#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop processes each test case and prints the minimum length of consecutive identical elements in the array `ar` for each test case. If the array consists of all identical elements or is empty, it prints `-1`. The variables `t`, `n`, and `a` retain their initial values, but the internal variables `same`, `num`, `minn`, and `i` are reset for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` and a list `a` of `n` integers. For each test case, it prints the minimum length of consecutive identical elements in the list `a`. If the list consists of all identical elements or is empty, it prints `-1`. The function does not return any value, and the input variables `t`, `n`, and `a` retain their initial values after the function concludes.

