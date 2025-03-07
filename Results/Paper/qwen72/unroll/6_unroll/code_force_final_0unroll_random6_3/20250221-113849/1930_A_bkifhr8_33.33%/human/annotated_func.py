#State of the program right berfore the function call: t is an integer where 1 <= t <= 5000, n is an integer where 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
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
        
    #State: `t` is an input integer where 1 <= t <= 5000, `n` is the last input integer where 1 <= n <= 50, `a` is a list of 2n integers where 1 <= a_i <= 10^7, `ans_f` is a list of `t` integers, each representing the sum of the minimum values of pairs from the corresponding input list `a`.
    for i in ans_f:
        print(i)
        
    #State: The loop has printed each integer in the list `ans_f`, where each integer is the sum of the minimum values of pairs from the corresponding input list `a`. The variables `t`, `n`, `a`, and `ans_f` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers from the input. It then calculates the sum of the minimum values of each pair of integers from the list and appends this sum to a list `ans_f`. After processing all test cases, it prints each integer in `ans_f`, where each integer represents the sum of the minimum values of pairs from the corresponding input list. The function does not return any value.

