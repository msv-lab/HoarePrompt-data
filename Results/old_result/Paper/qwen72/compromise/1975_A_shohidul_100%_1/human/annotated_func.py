#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^6, representing the elements of the array a.
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
        
    #State: After the loop executes all the iterations, `t` is 0, `_` is equal to `t` (the initial value of `t`), and for each test case, the conditions described in the initial and intermediate states are met. Specifically, for each test case, `n` is an input integer, `a` is a list of integers, and the program checks if the list `a` is non-decreasing. If it is, it prints 'YES'. If not, it checks if there is a valid split point where the remaining sublist is non-decreasing and all elements in this sublist are less than or equal to the first element of `a`. If such a split point exists, it prints 'YES'; otherwise, it prints 'NO'.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by an integer `n` (2 ≤ n ≤ 50) and a list `a` of `n` integers (1 ≤ a_i ≤ 10^6). The function reads the number of test cases `t` (1 ≤ t ≤ 1000) and then, for each test case, it checks if the list `a` is non-decreasing. If the list is non-decreasing, it prints 'YES'. If the list is not non-decreasing, it checks if there is a valid split point in the list such that the remaining sublist is non-decreasing and all elements in this sublist are less than or equal to the first element of `a`. If such a split point exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes without returning any value.

