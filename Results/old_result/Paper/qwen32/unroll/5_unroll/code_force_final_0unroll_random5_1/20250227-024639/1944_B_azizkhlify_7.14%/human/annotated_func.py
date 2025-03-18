#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 5 · 10^4) and an integer k (1 ≤ k ≤ ⌊n/2⌋). The array a is of length 2n and contains each integer from 1 to n exactly twice. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: A sequence of integers printed based on the conditions described in the code.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an integer `k`, along with an array `a` of length `2n` containing each integer from 1 to `n` exactly twice. For each test case, it prints a sequence of integers based on specific conditions related to the counts of elements in the first and second halves of the array. The function ensures that exactly `k` pairs or single elements are printed from the first half, and then prints the remaining elements to balance the counts from the second half if necessary.

