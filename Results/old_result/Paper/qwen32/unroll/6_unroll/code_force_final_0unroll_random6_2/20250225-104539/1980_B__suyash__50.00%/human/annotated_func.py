#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each of the t test cases, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: The state of the variables `t`, `n`, `f`, `k`, and `a` remains unchanged from the initial state, except that the outputs for each test case are printed. No other variables are affected by the loop.
    #
    #Output State:
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then determines whether the favorite element (at index `f-1` in the list `a`) can be among the top `k` elements when the list `a` is sorted in descending order. The function prints 'YES' if the favorite element is among the top `k` elements, 'NO' if it is not, and 'MAYBE' if the favorite element is exactly the `k`-th element and there are ties.

