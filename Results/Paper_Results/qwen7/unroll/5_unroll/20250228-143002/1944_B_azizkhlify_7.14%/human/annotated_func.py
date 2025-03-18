#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, an array a of length 2n is given, where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output state will consist of lines of output based on the given conditions within the loop. For each test case, it will first print pairs of numbers from the array `a` where the number appears exactly twice, up to `k` such pairs. If there are not enough such pairs to make `k`, it will then print additional single occurrences of numbers from the array `a` until `k` is satisfied. After that, it will print the remaining numbers from the array `a` that were part of the `res` list. If at any point the counts of left (`ul`) and right (`ur`) occurrences match, the loop breaks early. The final output will be a series of these printed lines for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \), an array \( a \) of length \( 2n \) where each integer from 1 to \( n \) appears exactly twice, and two integers \( n \) and \( k \). For each test case, it prints pairs of numbers from the array \( a \) where the number appears exactly twice, up to \( k \) such pairs. If there are not enough such pairs, it then prints additional single occurrences of numbers from the array \( a \) until \( k \) is satisfied. After that, it prints the remaining numbers from the array \( a \) that were part of the `res` list. If at any point the counts of left (`ul`) and right (`ur`) occurrences match, the loop breaks early. The function outputs a series of these printed lines for each test case.

