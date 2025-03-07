#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
def func():
    t = int(input())
    ans_f = []
    for i in range(t):
        ans = 0
        
        n = int(input())
        
        l = input()
        
        lst = l.split(' ')
        
        for i in range(n * 2):
            if len(lst) != 2:
                ans += min(int(lst[0]), int(lst[1]))
                lst.remove(lst[0 * 2])
                lst.remove(lst[1 * 2])
            else:
                ans += min(int(lst[0]), int(lst[1]))
                break
        
        ans_f.append(ans)
        
    #State: `t` is 0, `i` is `t` (which is 0), `n` is an input integer between 1 and 50 inclusive, `a` is a list of 2n integers where 1 <= a_i <= 10^7, `ans_f` contains the sum of the minimum values of pairs of integers from `lst` for each of the `t` iterations, and `lst` is either an empty list or a list with 2 elements for each iteration.
    for i in ans_f:
        print(i)
        
    #State: `t` is 0, `i` has iterated through all elements of `ans_f`, `ans_f` contains `n` elements, and `lst` is either an empty list or a list with 2 elements for each iteration.
#Overall this is what the function does:The function reads an integer `t` from the user, where `1 <= t <= 5000`. For each of the `t` test cases, it reads an integer `n` (where `1 <= n <= 50`) and a list of `2n` integers from the user. It then processes these integers by repeatedly selecting the minimum of the first two elements, summing these minimum values, and removing the selected elements until the list is either empty or contains only two elements. The function appends the sum of these minimum values to a list `ans_f` for each test case. After processing all test cases, the function prints each element in `ans_f`. The final state of the program is that `t` is 0, `ans_f` contains `t` elements, and the list `lst` is either empty or contains 2 elements for each iteration.

