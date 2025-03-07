#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}, and for each test case, a list of n integers a_1, a_2, ..., a_n is provided where 1 ≤ a_i ≤ 10^{12}. Additionally, the sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: Output State: `ans_list` contains the sum of `a[0]` repeated `n` times plus the total reduction in `res` over all iterations, adjusted by the final value of `res` and the final value of `ans`.
    #
    #To explain further, after all iterations of the loop, the list `ans_list` will contain the final computed value of `ans` for each iteration. The value of `ans` is calculated based on sorting the list `a`, then iteratively adjusting it based on the differences between consecutive elements and the value of `k`. After all iterations, `ans` is further adjusted by adding `(ans - 1) * (n - 1)` and the final value of `res`. The `res` variable keeps track of remaining reductions that couldn't be fully applied due to insufficient `k` values, which gets added to `ans` at the end.
    for a in ans_list:
        print(a)
        
    #State: Output State: `ans_list` will contain the final computed value of `ans` for each iteration after all iterations of the loop have finished. This value is determined by sorting the list `a`, then iteratively adjusting it based on the differences between consecutive elements and the value of `k`. After all iterations, `ans` is further adjusted by adding `(ans - 1) * (n - 1)` and the final value of `res`. The `res` variable keeps track of remaining reductions that couldn't be fully applied due to insufficient `k` values, which gets added to `ans` at the end.
    #
    #In natural language, the output state after the loop executes all its iterations means that `ans_list` will hold the final adjusted value of `ans` for each input list `a` after the loop has completed all its intended iterations. This final value of `ans` is derived from the sorted list `a`, with adjustments made during each iteration based on the differences between consecutive elements and the value of `k`. After processing all elements, any remaining reductions stored in `res` are also added to `ans`.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer \( t \), two integers \( n \) and \( k \), and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). For each test case, it sorts the list \( a \), then iteratively adjusts the first element of the list based on the differences between consecutive elements and the value of \( k \). After all adjustments, it calculates a final value for the first element of the list, which is influenced by the remaining value of \( k \) and the number of elements in the list. The function outputs the final value for each test case and returns a list containing these values.

