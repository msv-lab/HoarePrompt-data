#State of the program right berfore the function call: The function `func` is not properly defined in the context of the problem. The correct function definition should be `def find_subarrays(a, n, k):` where `a` is a list of integers of length `2n` containing each integer from 1 to `n` exactly twice, `n` is an integer such that 2 ≤ n ≤ 5 · 10^4, and `k` is an integer such that 1 ≤ k ≤ ⌊n/2⌋.
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
        
    #State: The loop will have processed all the test cases, and for each test case, it will have printed pairs of integers from the list `a` that appear twice in the first half of the list, followed by any remaining integers needed to reach the total count of `k * 2` from the first half of the list. After that, it will print any remaining integers needed to reach the total count of `k * 2` from the second half of the list. The variables `l`, `r`, `re`, `ul`, `ur`, and `res` will be reset for each test case, but the overall structure of the loop will remain the same.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes a list `a` of integers of length `2n` (where each integer from 1 to `n` appears exactly twice), an integer `n` (2 ≤ n ≤ 50,000), and an integer `k` (1 ≤ k ≤ ⌊n/2⌋). It prints pairs of integers from the first half of `a` that appear twice, followed by any remaining integers needed to reach a total of `2k` integers from the first half. It then prints any remaining integers needed to reach a total of `2k` integers from the second half of `a`. The function does not return any value.

