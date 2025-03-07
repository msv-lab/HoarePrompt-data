#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, each test case contains three integers n, f, and k such that 1 <= f, k <= n <= 100, and a list of n integers a_i such that 1 <= a_i <= 100.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        b = list(map(int, a.split()))
        
        o = input().split()
        
        n = b[0]
        
        f = b[1]
        
        k = b[2]
        
        if k == n:
            print('YES')
            continue
        
        fav = o[f - 1]
        
        dic = {i: o.count(i) for i in o}
        
        o.sort(reverse=True)
        
        if o.index(fav) > k - 1:
            print('NO')
            continue
        
        l = sorted(list(set(o)), reverse=True)
        
        for i in range(len(l)):
            if fav != l[i]:
                k -= dic[l[i]]
                if k <= 0:
                    print('NO')
                    break
            else:
                k -= dic[l[i]]
                if k < 0:
                    print('MAYBE')
                    break
                else:
                    print('YES')
                    break
        
    #State: The loop has completed all `t` iterations, and for each iteration, the variables `a`, `b`, `n`, `f`, `k`, `o`, `fav`, `dic`, and `l` have been updated as per the loop logic. The final state of `k` for each iteration depends on the counts of the strings in `l` and the initial value of `k`. The loop will have printed 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions met within the loop.
#Overall this is what the function does:The function processes a series of test cases. Each test case is defined by an integer `t` (1 <= t <= 1000), and for each test case, it reads three integers `n`, `f`, and `k` (1 <= f, k <= n <= 100) and a list of `n` integers. The function then determines if the `f`-th most frequent integer can be among the top `k` most frequent integers after sorting the list in descending order. For each test case, it prints 'YES' if the `f`-th most frequent integer is among the top `k`, 'NO' if it is not, and 'MAYBE' if it is among the top `k` but the remaining count of other integers is insufficient to displace it. After processing all test cases, the function concludes.

