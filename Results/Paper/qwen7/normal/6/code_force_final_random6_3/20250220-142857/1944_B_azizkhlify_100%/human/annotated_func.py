#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: The output will consist of pairs of identical numbers from the array `a`, printed in the order they are found, until `k` pairs have been printed. Once `k` pairs are printed, any remaining single occurrences of these numbers (from the first part of the array `a`) will be printed next, up to `k` such numbers. Finally, any pairs found in the second half of the array `a` will be printed, again in the order they are found, until `ul` (the count of pairs found in the first half) equals `ur` (the count of pairs found in the second half).
    #
    #To summarize, the output will be a sequence of pairs and single numbers from the array `a`, printed according to the rules specified in the loop, ensuring that all conditions for `k` pairs and `k` single numbers are met before moving on to the second half of the array. The exact content of the output will depend on the specific values of `n`, `k`, and the array `a`, but it will always follow the described pattern.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k, and an array a. For each test case, it prints pairs of identical numbers from the array a, up to k pairs, followed by any remaining single occurrences of these numbers, also up to k such numbers. After that, it prints any pairs found in the second half of the array a, up to when the count of pairs found in both halves of the array is equal. The output follows a specific pattern based on the values of n, k, and the array a, ensuring that the conditions for k pairs and k single numbers are met before moving on to the second half of the array.

