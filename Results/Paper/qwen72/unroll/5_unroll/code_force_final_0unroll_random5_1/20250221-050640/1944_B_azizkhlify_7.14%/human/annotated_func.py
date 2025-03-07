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
        
    #State: The list `a` remains unchanged. The variables `l` and `r` are updated to reflect the counts of each integer in the first and second halves of `a`, respectively. The variables `re`, `ul`, and `ur` are updated based on the number of integers printed. The list `res` contains the integers that were printed from the second loop.
#Overall this is what the function does:The function processes a list `a` of integers of length 2n, where each integer from 1 to n appears exactly twice, and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. It prints pairs of integers from the first half of `a` that appear exactly twice, up to `k` pairs. If fewer than `k` pairs are found, it prints additional integers from the first half of `a` that appear only once, up to the required count to reach `k` pairs. It then prints the same number of pairs from the second half of `a` to balance the output. The function does not return any value, and the list `a` remains unchanged.

