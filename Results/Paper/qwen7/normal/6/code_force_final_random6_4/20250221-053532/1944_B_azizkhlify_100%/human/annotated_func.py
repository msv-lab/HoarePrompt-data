#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, there is an array a of length 2n containing each integer from 1 to n exactly twice.
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
        
    #State: Output State: The loop has executed all its iterations, meaning it has processed all test cases provided as input. At the end of all iterations, `i` is `2 * n`, indicating that the loop has gone through all elements in the array `r`. The variable `res` contains all the elements that were printed during the loop's execution, which are pairs of identical numbers from the array `a` that appeared exactly twice, along with individual numbers from the second half of the array `a` that appeared exactly once up to the required count `k`. The variable `ur` is the total count of elements in `r` that correspond to indices `a[i] - 1` where `i` ranges from `n` to `2 * n - 1` and were set to 0, reflecting the count of elements in the second half of `a` that were printed. The loop ensures that all possible pairs and single occurrences are printed according to the rules specified, and `ur` reflects the final count of such elements from the second half of the array `a`.
#Overall this is what the function does:The function processes an array `a` of length 2n, where each integer from 1 to n appears exactly twice. It derives values `n` and `k` from the array length and range respectively. The function prints pairs of identical numbers from the first half of the array `a` that appear exactly twice, followed by individual numbers from the second half of the array `a` that appear exactly once up to the required count `k`. After processing all test cases, it prints the elements stored in the list `res`, which contain the pairs and single occurrences printed during the execution.

