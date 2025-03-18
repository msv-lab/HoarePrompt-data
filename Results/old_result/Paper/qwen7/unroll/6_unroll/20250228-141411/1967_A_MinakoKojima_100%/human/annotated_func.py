#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers satisfying 1 ≤ n ≤ 2·10^5 and 0 ≤ k ≤ 10^12, and a is a list of n integers where 1 ≤ a_i ≤ 10^12.
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
        
    #State: Output State: `ans_list` is a list containing integers calculated from the loop's logic, with each integer representing the final value of `ans` after processing each set of inputs provided by the loop. The value of `t` is reduced by one after each iteration, starting from the number of iterations specified by the first input. Each element in `ans_list` is derived from sorting the list `a`, calculating `ans` based on the differences between consecutive elements and the available `k`, and then updating `res` and `ans` accordingly.
    for a in ans_list:
        print(a)
        
    #State: [4, 2, 7, 1]
#Overall this is what the function does:The function processes a series of inputs defined by `t`, where `t` is the number of iterations. In each iteration, it reads two integers `n` and `k`, followed by a list `a` of `n` integers. It sorts the list `a` and calculates a value `ans` based on the differences between consecutive elements and the available `k`. It then updates `res` and `ans` accordingly. After processing all inputs, it prints the calculated values of `ans` for each iteration.

