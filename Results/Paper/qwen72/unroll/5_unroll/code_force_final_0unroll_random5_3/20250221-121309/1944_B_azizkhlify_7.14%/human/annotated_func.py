#State of the program right berfore the function call: Each test case contains two integers n and k such that 2 ≤ n ≤ 5 · 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is of length 2n and contains each integer from 1 to n exactly twice. The function should handle multiple test cases, with the number of test cases t satisfying 1 ≤ t ≤ 5000. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: The loop processes each test case and prints pairs or single elements from the array `a` based on the conditions. After all iterations, the variables `l`, `r`, `re`, `ul`, `ur`, and `res` will be reset for each new test case, but the overall structure and constraints of the initial state remain unchanged. The loop will have completed all its iterations, and the output will be the result of the print statements within the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and an array `a` of length `2n` containing each integer from 1 to `n` exactly twice. For each test case, it prints pairs or single elements from `a` based on specific conditions. The function does not return any value; instead, it prints the results directly. After processing all test cases, the function completes, and the output for each test case will be the elements printed according to the conditions specified within the function.

