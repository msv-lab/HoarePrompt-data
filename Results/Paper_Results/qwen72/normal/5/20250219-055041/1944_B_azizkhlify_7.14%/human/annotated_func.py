#State of the program right berfore the function call: a is a list of integers of length 2n where each integer from 1 to n appears exactly twice, and k is an integer such that 1 \leq k \leq \lfloor \frac{n}{2} \rfloor.
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
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: The loop has completed all iterations, and the final state of the variables is as follows:
#Overall this is what the function does:The function processes a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice, and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. It prints pairs of integers from the list `a` that appear twice, up to `k` pairs. If the number of pairs printed is less than `k`, it prints additional integers that appear only once, up to the remaining count needed to reach `k` pairs. Finally, it prints any remaining integers from the list `a` that were not printed in the first part. The function does not return any value.

