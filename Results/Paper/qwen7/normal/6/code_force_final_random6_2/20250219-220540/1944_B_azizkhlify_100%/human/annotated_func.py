#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The list a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: After the loop executes all the iterations, the value of `i` will be `2 * n`, `n` remains unchanged, `2 * n` remains unchanged, and `r[a[i] - 1]` for each `i` from `n` to `2 * n - 1` will be set to `0`. The loop will ensure that all elements in the list `a` are processed such that each unique element appears twice in the output. Specifically, the loop will print pairs of identical elements from the list `a` until the required number of unique elements (as specified by `k`) have been printed. Once `ul` (the count of elements printed as pairs) equals `ur` (the count of elements printed individually), the loop will terminate. The `res` list will contain all the unique elements from the list `a` that were printed individually. The final output will consist of all elements from the list `a` printed in pairs, followed by the elements in `res` printed individually.
    #
    #In summary, the output will be a sequence of pairs of identical elements from the list `a`, followed by the remaining unique elements from `a` that were not paired, ensuring every element from `a` is included in the output exactly twice.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice. It prints pairs of identical elements from the list until a specified number of unique elements (k) have been printed. Any remaining unique elements are printed individually at the end. The function ensures that each element from the list appears exactly twice in the output.

