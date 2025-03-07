#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each a_i is an integer such that 1 <= a_i <= 10^7.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 5000, `i` is `t - 1`, `n` is the integer input by the user such that 1 <= `n` <= 50, `a` is a list of 2n integers a_1, a_2, ..., a_{2n} where each a_i is an integer such that 1 <= a_i <= 10^7, `ans_f` is a list containing `t` elements, each being the sum of the minimums of all pairs of elements processed in each iteration, `l` is the string input by the user, and `lst` is either an empty list or a list of two elements.
    for i in ans_f:
        print(i)
        
    #State: All elements in `ans_f` have been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then calculates the sum of the minimums of all pairs of integers from the list and prints this sum for each test case.

