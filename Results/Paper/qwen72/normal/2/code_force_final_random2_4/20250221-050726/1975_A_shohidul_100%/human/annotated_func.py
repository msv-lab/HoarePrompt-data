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
        
    #State: _ is t-1, `t` is an integer where 1 ≤ t ≤ 1000, `n` is an input integer, `a` is a list of integers read from the input. For each test case, if `check_all` is `True`, the list `a` is non-decreasing from index 1 to `n-1`. If `check_all` is `False`, the loop has checked each pair of consecutive elements in the list `a` from index 1 to `n-1`. If any `a[i - 1]` > `a[i]` during the loop, `new` is a list containing all elements of `a` starting from the index where the condition was met to the end of the list, `check_all_new` is `True` if all elements in `new` are less than or equal to `a[0]`, otherwise `False`, `new_all` is `True` if all elements in `new` are in non-decreasing order, otherwise `False`. The loop will print 'YES' if both `check_all_new` and `new_all` are `True`, otherwise it will print 'NO'. The loop will terminate after the first iteration where `a[i - 1]` > `a[i]` is true, or after checking all pairs of consecutive elements in the list `a` from index 1 to `n-1`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50) and a list `a` of `n` integers (1 ≤ a_i ≤ 10^6). For each test case, it checks if the list `a` can be made non-decreasing by removing zero or one element. If the list can be made non-decreasing, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function terminates.

