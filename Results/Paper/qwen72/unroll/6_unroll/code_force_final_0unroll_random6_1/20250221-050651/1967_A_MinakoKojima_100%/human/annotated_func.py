#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers for each test case where 1 ≤ n ≤ 2·10^5 and 0 ≤ k ≤ 10^12, and a is a list of n integers where 1 ≤ a_i ≤ 10^12.
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
        
    #State: `ans_list` is a list containing the results of the loop for each test case, where each result is an integer representing the final value of `ans` after processing the corresponding test case. The values of `t`, `n`, `k`, and `a` are not retained after the loop completes, as they are re-initialized for each test case.
    for a in ans_list:
        print(a)
        
    #State: The values in `ans_list` are printed one by one, and the state of `ans_list` remains unchanged.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of an integer `n`, an integer `k`, and a list of `n` integers `a`. For each test case, it processes the list `a` to compute a final integer value `ans` based on the values of `a` and `k`. The function then appends this computed value to a list `ans_list`. After processing all test cases, the function prints each value in `ans_list` one by one. The final state of the program is that `ans_list` contains the results for each test case, and these results are printed to the console. The original input values `t`, `n`, `k`, and `a` are not retained after the function completes.

