#State of the program right berfore the function call: a is a list of integers of length 2n, where each integer from 1 to n appears exactly twice, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋.
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
        
    #State: a is a list of integers of length 2n, where each integer from 1 to n appears exactly twice, but the first k * 2 elements (if k * 2 ≤ n) or the first k elements (if k * 2 > n) have been printed and removed from the list. The remaining elements in the list are still in their original positions. k is an integer such that 1 ≤ k ≤ ⌊n/2⌋, and the values of l, r, re, ul, ur, and res are modified based on the loop execution.
#Overall this is what the function does:The function `func` processes a series of inputs where each input consists of an integer `n` and an integer `k`, followed by a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice. The function prints pairs of integers from the list `a` such that each integer appears exactly twice, up to a total of `k * 2` integers. If fewer than `k * 2` integers are printed, it continues to print single integers from the list until the total number of printed integers equals `k * 2`. The function does not return any value but modifies the state of the program by printing the selected integers and potentially altering the internal variables used for tracking. After the function concludes, the list `a` remains unchanged, but the internal variables `l`, `r`, `re`, `ul`, `ur`, and `res` are modified as part of the execution process.

