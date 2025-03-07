#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def find_subarrays(a, n, k):` where `a` is a list of integers of length 2n, `n` is a positive integer, and `k` is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The list `a` contains each integer from 1 to n exactly twice.
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
        
    #State: The loop has completed all iterations, and the final state is as follows:
#Overall this is what the function does:The function `find_subarrays` processes a list `a` of integers of length 2n, a positive integer `n`, and an integer `k` such that 1 ≤ k ≤ ⌊n/2⌋. It prints subarrays from `a` where each subarray contains exactly two occurrences of each integer from 1 to k, and the total length of these subarrays is 2k. If the required subarrays cannot be fully formed from the first half of `a`, it prints additional integers from the first half to meet the 2k length requirement. It also prints the remaining integers from the second half of `a` that have not been used in the subarrays. The function does not return any value.

