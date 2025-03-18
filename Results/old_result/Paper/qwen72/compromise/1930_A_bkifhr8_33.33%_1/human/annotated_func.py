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
        
    #State: `i` is `t - 1`, `n` is an input integer where 1 <= n <= 50, `ans_f` is a list of `t` integers, each representing the sum of the minimum values of pairs of integers from the corresponding `lst` until `lst` has 2 or fewer elements. `lst` is a list with 2 or fewer elements remaining for each iteration, and the loop has completed all `t` iterations.
    for i in ans_f:
        print(i)
        
    #State: `i` is the last element of `ans_f`, `n` is an input integer where 1 <= n <= 50, `ans_f` is a list of `t` integers where `t` must be greater than 0.
#Overall this is what the function does:The function reads an integer `t` from the input, where `1 <= t <= 5000`. For each of the `t` test cases, it reads another integer `n` (where `1 <= n <= 50`) and a list of `2n` integers (each between `1` and `10^7`). The function then processes each list by repeatedly removing the two smallest elements and adding the smaller of the two to a running sum until the list has 2 or fewer elements remaining. The final sum for each test case is appended to a list `ans_f`. After processing all `t` test cases, the function prints each element of `ans_f`. The final state of the program is that `ans_f` is a list of `t` integers, and the input has been fully consumed.

