#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output will consist of multiple lines, each representing the result of one test case. For each test case, the output will contain pairs of integers printed on separate lines, where each pair represents two occurrences of the same integer from the array `a`. The pairs are printed in the order they appear in the array `a`, and the process stops once `k` pairs have been printed or when there are no more pairs left to print. Any remaining integers that were not printed as pairs will be listed at the end of the line. If the counts of pairs found in the first half (`l`) and the second half (`r`) of the array do not match, the script will continue to print pairs from the second half until the counts match.
    #
    #In simpler terms, the output will show pairs of identical numbers from the array `a` as specified by `k`, and any leftover numbers that couldn't form pairs will be listed at the end.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice, along with two integers n and k. It prints pairs of identical numbers from the array `a` as specified by `k`, and any leftover numbers that couldn't form pairs are listed at the end. If the counts of pairs found in the first half and the second half of the array do not match, it continues to print pairs from the second half until the counts match.

