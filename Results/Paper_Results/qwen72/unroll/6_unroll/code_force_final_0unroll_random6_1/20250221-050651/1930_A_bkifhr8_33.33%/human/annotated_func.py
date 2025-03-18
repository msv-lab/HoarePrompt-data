#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, n is an integer where 1 ≤ n ≤ 50, and a is a list of 2n integers where 1 ≤ a_i ≤ 10^7.
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
        
    #State: t is an input integer where 1 ≤ t ≤ 5000, n is an integer where 1 ≤ n ≤ 50, a is a list of 2n integers where 1 ≤ a_i ≤ 10^7, ans_f is a list of t integers where each integer is the sum of the minimum values of pairs of integers from the input list a.
    for i in ans_f:
        print(i)
        
    #State: The loop prints each integer in the list `ans_f`, which contains the sums of the minimum values of pairs of integers from the input list `a`. The values of `t`, `n`, `a`, and `ans_f` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 5000) indicating the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 50) and a list of 2n integers (1 ≤ a_i ≤ 10^7). It then calculates the sum of the minimum values of each pair of integers from the list and appends these sums to a list `ans_f`. Finally, it prints each integer in `ans_f`. The function does not return any value.

