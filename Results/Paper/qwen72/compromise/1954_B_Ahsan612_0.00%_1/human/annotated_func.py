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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `a` is a list of integers of length n where 1 ≤ a_i ≤ n, `ar` is a list of integers input by the user with at least 2 elements, `i` is equal to `len(ar)`, `num` is the last element of `ar`, `minn` is the minimum length of any sequence of consecutive identical elements in `ar`, and `same` is 1. If `minn` was initially `inf`, it is updated to the length of the first sequence of consecutive identical elements found in `ar`. If no such sequence is found, `minn` remains `inf` and the output is `-1`. Otherwise, `minn` is not equal to `inf` and the output is the value of `minn`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of integers `ar` of length `n`. It then finds the minimum length of any sequence of consecutive identical elements in `ar`. If no such sequence exists, it prints `-1`. Otherwise, it prints the length of the shortest sequence of consecutive identical elements. After processing all test cases, the function concludes, and the state of the program includes the number of test cases `t`, the number of elements `n` for the last test case, the list `ar` of integers input for the last test case, and the variables `i`, `num`, `minn`, and `same` which are updated during the processing of the last test case.

