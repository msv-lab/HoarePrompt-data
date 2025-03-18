#State of the program right berfore the function call: a is a list of integers of length 2n where each integer from 1 to n appears exactly twice, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋.
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
        
    #State: The list `a` remains unchanged. The variables `l` and `r` are lists of length `n` where each element is either 0 or 1, depending on whether the corresponding integer in `a` has been fully processed or not. The variables `re`, `ul`, and `ur` are integers representing the number of elements processed in the respective parts of the loop. The list `res` contains the integers that were printed in the second part of the loop, if any.
#Overall this is what the function does:The function `func` processes a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice, and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. It prints pairs of integers from the first half of `a` until `k` pairs are printed or all pairs are exhausted. If more pairs are needed, it prints single integers from the first half of `a` until the required number of elements is printed. Finally, it prints pairs of integers from the second half of `a` to balance the number of printed elements from both halves. The list `a` remains unchanged, and no value is returned.

