#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n positive integers such that 1 ≤ a_i ≤ 10^6 for all i.
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
        
    #State: The output will be 'YES' if the list `a` is either non-decreasing or can be split into two segments where the first segment is non-increasing and the second segment is non-decreasing. Otherwise, it will be 'NO'.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes a list of `n` positive integers (`a`) and an integer `t`. It checks if the list `a` is non-decreasing or can be split into two segments where the first segment is non-increasing and the second segment is non-decreasing. If any of these conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function returns nothing but prints the result for each test case.

