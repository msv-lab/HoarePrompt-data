#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: The loop has completed all `t` iterations, and for each iteration, the final state includes `i` being the length of `l` minus 1, `k` being the initial `k` minus the sum of the counts of all strings in `l` that are not equal to `fav` and minus the count of `fav` if `fav` is in `l`. The loop will have printed 'NO' if `k` became less than or equal to 0 before reaching `fav` in the list `l`, 'MAYBE' if `k` became less than 0 when `fav` was encountered, and 'YES' if `k` was greater than or equal to 0 when `fav` was encountered.
#Overall this is what the function does:The function reads `t` test cases from the user. For each test case, it reads two lines of input: the first line contains three integers `n`, `f`, and `k`, and the second line contains a list of `n` integers. It then checks if the `f`-th element in the sorted list of integers (in descending order) can be included in the top `k` elements based on their frequency. If `k` equals `n`, it prints 'YES'. If the `f`-th element is not among the top `k` elements, it prints 'NO'. If the `f`-th element is among the top `k` elements but the remaining elements have a combined frequency that exceeds `k`, it prints 'MAYBE'. Otherwise, it prints 'YES'. After processing all test cases, the function ends.

