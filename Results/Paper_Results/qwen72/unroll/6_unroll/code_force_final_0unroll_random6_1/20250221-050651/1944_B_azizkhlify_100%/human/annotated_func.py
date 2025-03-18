#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n and k are integers for each test case where 2 <= n <= 5 * 10^4 and 1 <= k <= floor(n/2), and a is a list of 2n integers where 1 <= a_i <= n and each integer from 1 to n appears exactly twice in a.
def func():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        
        a = [int(i) for i in input().split()]
        
        l = [0] * n
        
        r = [0] * n
        
        re = ul = ur = 0
        
        res = []
        
        for i in range(n):
            l[a[i] - 1] += 1
        
        for i in range(n, 2 * n):
            r[a[i] - 1] += 1
        
        for i in range(n):
            if l[a[i] - 1] == 2:
                print(a[i], a[i], end=' ')
                l[a[i] - 1] = 0
                ul += 2
            if ul == k * 2:
                break
        
        k = 2 * k - ul
        
        if k:
            for i in range(n):
                if l[a[i] - 1] == 1:
                    print(a[i], end=' ')
                    re += 1
                    res.append(a[i])
                if re == k:
                    break
        
        print()
        
        for i in res:
            print(i, end=' ')
        
        if ul != ur:
            for i in range(n, 2 * n):
                if r[a[i] - 1] == 2:
                    print(a[i], a[i], end=' ')
                    r[a[i] - 1] = 0
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: The loop will print pairs of integers and single integers from the list `a` based on the conditions provided. After all iterations, the variables `l`, `r`, `re`, `ul`, `ur`, and `res` will be modified, but the initial variables `t`, `n`, and `k` will remain unchanged. The exact final values of `l`, `r`, `re`, `ul`, `ur`, and `res` depend on the input values and the specific elements in the list `a`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list `a` of 2n integers. For each test case, it prints pairs of integers from the list `a` that appear twice, up to a total of `k` pairs. If there are not enough pairs to satisfy `k`, it prints additional single integers to meet the total count of `2k`. The function ensures that the pairs and single integers are printed in the order they appear in the list `a`. After processing all test cases, the initial variables `t`, `n`, and `k` remain unchanged, but the auxiliary variables `l`, `r`, `re`, `ul`, `ur`, and `res` are modified.

