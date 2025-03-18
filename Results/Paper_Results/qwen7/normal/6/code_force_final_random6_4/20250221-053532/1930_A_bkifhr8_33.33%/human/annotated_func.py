#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: `ans_f` contains the sum of the minimum values between pairs of elements from the list `lst` for each iteration of the loop, until the length of `lst` is less than 2, for all iterations specified by `t`.
    for i in ans_f:
        print(i)
        
    #State: `ans_f` must be an empty list.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and \( 2n \) integers \( a_1, a_2, \ldots, a_{2n} \). It then calculates the sum of the minimum values of each pair of consecutive integers from the list \( a_1, a_2, \ldots, a_{2n} \) until fewer than two integers remain. The results for each test case are stored in a list and printed out. After processing all test cases, the list containing the results is empty.

