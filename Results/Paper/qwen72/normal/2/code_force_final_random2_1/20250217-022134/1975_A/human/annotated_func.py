#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^6, representing the elements of the array a.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] <= a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all_new = all([(a[0] >= new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all_new and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: After all iterations of the loop, `t` must be at least 1, `_` is a throwaway variable, `n` is an input integer, `a` is a list of integers from the input, `i` is `n-1`. For each iteration, if `a` is non-decreasing (`check_all` is `True`), 'YES' is printed. If `a` is not non-decreasing (`check_all` is `False`), the loop checks if the sub-list `new` (starting from the first decrease) is non-decreasing and all elements in `new` are less than or equal to `a[0]`. If both conditions are met, 'YES' is printed; otherwise, 'NO' is printed. The loop iterates `t` times, and the final state reflects the results of these checks for each input list `a`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. The function checks if the list `a` is non-decreasing. If it is, the function prints 'YES'. If not, it checks if the list can be split into two parts such that the second part is non-decreasing and all elements in the second part are less than or equal to the first element of the original list. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. This process is repeated for each of the `t` test cases. After processing all test cases, the function has printed 'YES' or 'NO' for each test case based on the conditions described.

