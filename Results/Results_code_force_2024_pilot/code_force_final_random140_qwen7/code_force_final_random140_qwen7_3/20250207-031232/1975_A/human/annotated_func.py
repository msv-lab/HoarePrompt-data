#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n positive integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] < a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all = all([(a[0] > new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: Output State: `t` must be exactly equal to the number of times the loop was executed, `i` equals `n`, `new` is an empty list, `new_all` is either `None` or a boolean value indicating whether the elements in `new` are non-decreasing, `a` is a list of integers obtained from input using `map(int, input().split())`, and `check_all` retains its last evaluated value (which could be True or False depending on the input list `a`).
    #
    #In natural language, this means that after all iterations of the loop have finished, the variable `t` will be equal to the total number of times the loop was executed. The variable `i` will always be equal to `n`, where `n` is the length of the list `a`. The variable `new` will be an empty list since it is only assigned when a certain condition is met within the loop, but that condition never leads to `new` being assigned across multiple iterations. The variable `new_all` will either be `None` (if `new` was never assigned) or a boolean value indicating whether the elements in `new` are in non-decreasing order. The list `a` will contain the integers input by the user, and `check_all` will hold the final result of the condition checked in the first part of the loop, which could be either `True` or `False` based on the input list `a`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` positive integers `a`. It checks if the list `a` is strictly increasing. If not, it further checks if removing the first element and checking the remaining list results in a non-decreasing list. Based on these checks, it prints 'YES' if the conditions are met, otherwise it prints 'NO'. After processing all test cases, it outputs the final results for each case.

