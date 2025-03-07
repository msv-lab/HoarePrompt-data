#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: All pairs from the left half that appear exactly twice are printed. All singles from the left half that appear exactly once are printed. All pairs from the right half that appear exactly twice are printed if ul is not equal to ur.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and an array `a` of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it prints pairs of integers from the left half of the array that appear exactly twice, up to `k` pairs. If fewer than `k` pairs are found, it prints single integers from the left half that appear exactly once until the total count of printed numbers reaches `2k`. If the number of printed pairs from the left half does not match the number of printed pairs from the right half, it prints pairs from the right half that appear exactly twice until the counts match.

