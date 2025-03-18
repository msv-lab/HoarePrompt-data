#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: The loop has executed all iterations, and the final value of `t` is 0. `n` is the length of the list `a`, which may vary depending on the input. `check_all` remains unchanged from its last known state, and `i` is now equal to `n`. If the loop did not break early, `check_all` will be `True`, meaning all elements in `a` satisfy the condition `a[i-1] <= a[i]` for all `i` from 1 to `n`. If the loop breaks early, `check_all` will be `False`, indicating that there exists at least one pair of consecutive elements in `a` that does not satisfy the condition.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, an integer `n`, and a list `a` of `n` integers. For each test case, it checks if the list `a` is non-decreasing (i.e., each element is less than or equal to the next element). If the list is non-decreasing, it prints 'YES'. If not, it checks if the list can be split into two parts where the first part is non-increasing and the second part is non-decreasing. If such a split exists, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

