#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers satisfying 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}, and a is a list of n integers where 1 ≤ a_i ≤ 10^{12}.
def func():
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: Output State: `ans_list` is a list containing integers calculated from the loop executions, with each element representing the final value of `ans` for each input iteration. The value of `t` is the number of iterations in the loop, and for each iteration, `n`, `k`, and `a` are updated based on user input, leading to a different `ans` value which is then appended to `ans_list`.
    for a in ans_list:
        print(a)
        
    #State: The output state will remain the same as the initial state because the loop does not modify any variables or perform any operations that change the values within `ans_list`. The loop simply iterates over the elements in `ans_list` and prints them, but it does not alter the contents of `ans_list`.
#Overall this is what the function does:The function processes `t` iterations of input data consisting of integers `n`, `k`, and a list `a` of `n` integers. For each iteration, it calculates a value `ans` based on the sorted list `a` and the integer `k`. The function then appends each calculated `ans` to a list `ans_list`. Finally, it prints each value in `ans_list`. The function returns nothing but modifies and outputs a list of calculated values.

