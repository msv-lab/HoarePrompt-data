#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, an array a of length 2n is given, where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output will consist of lines corresponding to each test case. For each test case, it will print pairs of integers from the array `a` that appear exactly twice, followed by any single integers that appear once, up to `k` such integers. After that, it will print the remaining single integers. If the count of pairs (`ul`) does not match the count of single integers (`ur`), it will continue printing pairs until they match.
    #
    #In more detail, for each test case:
    #- It first prints pairs of integers that appear exactly twice, up to `k` pairs.
    #- Then it prints up to `k` single integers that appear once.
    #- Finally, it prints any remaining single integers.
    #
    #This process ensures that the output respects the constraints on `n`, `k`, and the structure of the array `a`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( t \) (the number of test cases), \( n \) (the size of the array divided by 2), \( k \) (an integer constraint), and an array \( a \) of length \( 2n \) where each integer from 1 to \( n \) appears exactly twice. For each test case, it prints pairs of integers from \( a \) that appear exactly twice, up to \( k \) pairs. Then, it prints up to \( k \) single integers that appear once. Finally, it prints any remaining single integers. If the count of pairs does not match the count of single integers, it continues printing pairs until they match.

