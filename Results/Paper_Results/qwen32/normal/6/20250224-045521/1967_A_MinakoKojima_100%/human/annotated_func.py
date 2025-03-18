#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each integer a_i is such that 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: `ans_list` contains the final answers for all test cases, and other variables reflect the state after the last test case.
    for a in ans_list:
        print(a)
        
    #State: All elements in `ans_list` have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a result based on the values of `n`, `k`, and the sorted list `a`. The result is derived by adjusting the smallest element in the list and distributing `k` across the differences between consecutive elements, then adding additional calculations based on the remaining `k` and the number of unique differences.

