#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, for each test case, n is an integer such that 1 <= n <= 2 * 10^5, k is an integer such that 0 <= k <= 10^12, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: ans_list is a list of final ans values for each test case.
    for a in ans_list:
        print(a)
        
    #State: The output state remains the same as the initial state, with ans_list still being a list of final ans values for each test case. The only change is that each value in ans_list has been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a value `ans` based on the given inputs. The final state of the program is that it outputs the calculated `ans` for each test case.

