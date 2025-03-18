#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and a is a list of n integers where 1 <= a_i <= 10^6.
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
        
    #State: The values of `t`, `n`, and `a` remain unchanged. The loop prints 'YES' or 'NO' for each iteration based on the conditions described in the loop.
#Overall this is what the function does:The function `func` reads input values for `t`, `n`, and `a` from the user. It processes `t` test cases, where for each test case, it checks if the list `a` of `n` integers is either non-decreasing or can be made non-decreasing by removing the first element. If the list meets either of these conditions, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the values of `t`, `n`, and `a` are not retained as they are re-assigned within each iteration of the loop.

