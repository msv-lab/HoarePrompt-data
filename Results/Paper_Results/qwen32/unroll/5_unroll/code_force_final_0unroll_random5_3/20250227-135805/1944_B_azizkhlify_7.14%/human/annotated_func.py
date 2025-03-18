#State of the program right berfore the function call: Each test case consists of two integers n and k where 2 ≤ n ≤ 5 · 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The second line contains 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ n, and every integer from 1 to n occurs exactly twice in a. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, and a list of `2n` integers `a` where each integer from 1 to `n` appears exactly twice. It prints pairs of equal integers from the list, ensuring that the indices of the pairs are at most `k` positions apart. After printing such pairs from the first half of the list, it prints additional pairs from the second half if needed to balance the output.

