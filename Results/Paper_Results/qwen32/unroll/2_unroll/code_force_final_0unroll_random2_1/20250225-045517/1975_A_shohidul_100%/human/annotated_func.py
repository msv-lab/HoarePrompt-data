#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: The output state consists of `t` lines, each either 'YES' or 'NO', corresponding to each test case. For each test case, 'YES' is printed if the list `a` is non-decreasing or can be made non-decreasing by removing a prefix of elements such that the remaining list is non-decreasing and the first element of the original list is greater than or equal to all elements of the new list. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it determines if the list `a` is non-decreasing or can be made non-decreasing by removing a prefix of elements such that the remaining list is non-decreasing and the first element of the original list is greater than or equal to all elements of the new list. It outputs 'YES' if either condition is met, otherwise 'NO'.

