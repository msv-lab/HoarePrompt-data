#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each a_i is such that 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: `ans_list` contains the final results for each test case, and other variables like `t`, `n`, `k`, and `a` retain their values from the last test case.
    for a in ans_list:
        print(a)
        
    #State: ans_list contains the final results for each test case, and other variables like t, n, k, and a retain their values from the last test case. The loop has printed each element of ans_list to the console.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. For each test case, it calculates a result based on the values of `n`, `k`, and `a`, and prints this result. The final state of the program is that it has printed the result for each test case.

