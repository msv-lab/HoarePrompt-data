#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins available to buy new cards, respectively. a is a list of n integers, each a_i where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `_` is `t - 1`, `n` and `k` are input integers, `a` is a sorted list of integers derived from the input, `i` is `n - 2`, `ans` is the final value after all iterations plus `(ans - 1) * (n - 1) + res`, `res` is the final value after all iterations plus `k % n` if `k` is not 0, otherwise `res` remains the final value after all iterations, `k` is 0 or the remaining value after the last iteration, `ans_list` contains `t` elements, each being the value of `ans` for each test case.
    for a in ans_list:
        print(a)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `_` is `t - 1`, `n` and `k` are input integers, `a` is a sorted list of integers derived from the input, `i` is `n - 2`, `ans` is the final value after all iterations plus `(ans - 1) * (n - 1) + res`, `res` is the final value after all iterations plus `k % n` if `k` is not 0, otherwise `res` remains the final value after all iterations, `k` is 0 or the remaining value after the last iteration, `ans_list` contains `t` elements, each being the value of `ans` for each test case, `a` is the last element in `ans_list`, `ans_list` must have exactly `t` elements.
#Overall this is what the function does:The function processes a series of test cases, each defined by the number of distinct types of cards `n`, the number of coins available `k`, and a list `a` of the number of cards of each type. For each test case, it calculates the maximum number of distinct types of cards that can be obtained by using the available coins to buy additional cards. The function then prints the result for each test case. After processing all test cases, the function ensures that `t` results are printed, where `t` is the number of test cases.

