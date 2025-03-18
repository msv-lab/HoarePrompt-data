#State of the program right berfore the function call: The function is expected to handle multiple test cases, where `t` is an integer such that 1 ≤ t ≤ 10^4. For each test case, `n` is an integer such that 1 ≤ n ≤ 3 · 10^5, and `a` is a list of `n` integers such that 1 ≤ a_i ≤ n. The array `a` is guaranteed to be beautiful, and the sum of `n` over all test cases does not exceed 3 · 10^5.
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
        
    #State: For each test case, the loop will print the minimum length of consecutive segments of the same number in the array `ar`. If the array `ar` consists of a single unique number repeated, it will print `-1`. The variables `t`, `n`, and `a` will remain unchanged as they are input variables. The loop variables `same`, `num`, `minn`, and `i` will be reset for each test case, and their final values after the loop will not be meaningful outside the context of the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints the minimum length of consecutive segments of the same number in the list `a`. If the list `a` consists of a single unique number repeated throughout, it prints `-1`. The function does not return any value, and the input variables `t`, `n`, and `a` remain unchanged. The internal loop variables are reset for each test case and do not retain meaningful values after the function concludes.

