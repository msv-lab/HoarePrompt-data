#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The values of `t`, `n`, `f`, `k`, and `a` remain unchanged. The loop iterates `t` times, and during each iteration, it reads input values for `a` and `o`, processes them, and prints 'YES', 'NO', or 'MAYBE' based on the conditions specified in the loop. After all iterations, the initial values of `t`, `n`, `f`, `k`, and `a` are still the same as they were before the loop started.
#Overall this is what the function does:The function `func` reads `t` test cases from the user input. For each test case, it reads two lines of input: the first line contains three integers `n`, `f`, and `k`, and the second line contains a list of `n` integers. The function then determines if the `f`-th element in the list (considering 1-based indexing) can be among the top `k` elements after sorting the list in non-increasing order. It prints 'YES' if the `f`-th element is within the top `k` elements, 'NO' if it is not, and 'MAYBE' if the `f`-th element is exactly at the `k`-th position but the count of elements equal to or greater than it is insufficient to fill the top `k` positions. The function does not return any value. After all iterations, the initial values of `t`, `n`, `f`, `k`, and `a` remain unchanged.

