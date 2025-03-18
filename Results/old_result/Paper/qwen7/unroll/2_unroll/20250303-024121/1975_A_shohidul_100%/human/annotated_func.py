#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: The output state depends on the input values of `t`, `n`, and `a` for each iteration of the loop. For each `t` iterations, the program checks if the list `a` is non-decreasing. If it is, it prints 'YES'. Otherwise, it checks if there exists a subsequence starting from any index that is non-decreasing and its first element is greater than or equal to the rest of the elements in the subsequence. If such a subsequence exists, it prints 'YES'; otherwise, it prints 'NO'.
    #
    #Since the exact input values are not provided, the output state cannot be precisely determined without knowing the specific values of `t`, `n`, and `a` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list \( a \) of \( n \) integers. For each test case, it checks if the list \( a \) is non-decreasing. If it is, it prints 'YES'. Otherwise, it checks if there exists a subsequence starting from any index that is non-decreasing and whose first element is greater than or equal to the rest of the elements in the subsequence. If such a subsequence exists, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

