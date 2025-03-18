#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, there is an array a of length 2n where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The loop has executed all its iterations, and the final state of the variables is as follows:
    #
    #- `i` is `2 * n`.
    #- `res` is an empty list.
    #- Both `ul` and `ur` are equal to the total number of pairs (2 * k) found in the array `a` where an element appears exactly twice.
    #- All elements that satisfy the conditions specified in the loop body have been printed.
    #
    #This means that after processing all elements in the array `a`, the loop has identified and printed all pairs of identical elements up to `k` pairs, and any remaining elements that were part of pairs but not fully printed due to the stopping conditions have also been accounted for.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \) and \( k \), and an array \( a \) of length \( 2n \) where each integer from 1 to \( n \) appears exactly twice. For each test case, it identifies and prints up to \( k \) pairs of identical elements from the array \( a \). If there are not enough pairs to form \( k \) pairs, it prints as many pairs as possible. After processing, it prints the remaining elements that were part of pairs but not fully printed due to the stopping conditions.

