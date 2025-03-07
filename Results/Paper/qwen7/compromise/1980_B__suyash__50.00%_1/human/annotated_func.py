#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i in range n.
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
        
    #State: i is 9, l has been fully traversed (i.e., i is equal to or exceeds the length of l - 1), k is decreased by the sum of dic[l[i]] for all i from 0 to 8, and the final value of k is greater than or equal to 0.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it checks if a specific element `fav` in a sorted list `o` can be moved up to position `k` without violating certain conditions. If `fav` can be moved up to or beyond position `k`, it prints 'YES'. If `fav` cannot be moved up to position `k` but can be moved up to some other position, it prints 'MAYBE'. If `fav` cannot be moved up to any position beyond `k`, it prints 'NO'. The function performs these checks for each test case and continues to the next one until all test cases are processed.

