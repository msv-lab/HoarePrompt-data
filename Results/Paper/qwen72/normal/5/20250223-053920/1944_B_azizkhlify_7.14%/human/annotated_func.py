#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n and k are integers for each test case where 2 <= n <= 5 * 10^4 and 1 <= k <= floor(n/2), and a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: The variables `t`, `n`, `k`, and `a` retain their initial values. The variables `l` and `r` are lists of length `n` where each element represents the count of the corresponding integer in the first and second halves of the list `a`, respectively. The variables `re`, `ul`, and `ur` are updated to reflect the number of elements printed from the first and second halves of the list `a`. The list `res` contains the elements printed from the first half of the list `a` that were not fully printed in pairs.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list `a` of 2n integers. For each test case, it prints pairs of integers from the first half of `a` that appear exactly twice, until `k` pairs are printed or no more such pairs are available. If additional unique elements are needed to reach a total of `k` pairs, it prints single elements from the first half of `a`. It then prints the remaining elements from the second half of `a` that were not fully printed in pairs. The function does not return any value; it only prints the results. After the function concludes, the variables `t`, `n`, `k`, and `a` retain their initial values, while `l`, `r`, `re`, `ul`, and `ur` are updated to reflect the counts and the number of elements printed.

