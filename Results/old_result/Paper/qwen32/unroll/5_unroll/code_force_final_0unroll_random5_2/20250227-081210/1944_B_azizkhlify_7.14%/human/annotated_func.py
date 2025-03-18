#State of the program right berfore the function call: Each test case consists of two integers n and k where 2 ≤ n ≤ 5 · 10^4, and 1 ≤ k ≤ ⌊n/2⌋. The test case is followed by a list of 2n integers a_1, a_2, ..., a_{2n} where each integer from 1 to n occurs exactly twice. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: the sequence of numbers printed by the code execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, and a list of `2n` integers where each integer from 1 to `n` appears exactly twice. For each test case, it prints a sequence of numbers based on the values of `n` and `k`. Specifically, it first prints up to `2k` numbers that appear exactly twice in the first half of the list, then up to `k` numbers that appear exactly once in the first half, and finally prints the remaining numbers that appear exactly twice in the second half of the list to ensure the total count of printed numbers matches `2k`.

