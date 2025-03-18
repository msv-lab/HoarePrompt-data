#State of the program right berfore the function call: Each test case contains an integer n (2 ≤ n ≤ 5 · 10^4) and an integer k (1 ≤ k ≤ ⌊n/2⌋). The array a consists of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: The output state consists of numbers printed in the specified format, with pairs printed first from the first half of the array, followed by individual numbers from the first half if needed, and finally pairs from the second half if the counts do not match.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and an array `a` of `2n` integers where each integer from 1 to `n` appears exactly twice. For each test case, it prints `k` pairs of numbers from the first half of the array, followed by up to `k` individual numbers from the first half if needed, and finally pairs from the second half if the counts do not match. The output is formatted such that pairs are printed first, followed by individual numbers, and then additional pairs from the second half if necessary.

