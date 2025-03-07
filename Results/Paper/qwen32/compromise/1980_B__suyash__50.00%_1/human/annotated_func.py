#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: i is `t - 1`, `a`, `b`, `o`, `n`, `f`, `k`, `fav`, `dic`, and `l` reflect the state of the last test case processed, and the final print statement ("YES", "NO", or "MAYBE") has been executed for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines if a favorite element (specified by `f`) can be among the top `k` elements in the list `a` after sorting, and prints "YES", "NO", or "MAYBE" based on the conditions met.

