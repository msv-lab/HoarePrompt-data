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
        
    #State: Output State: The loop will have processed all test cases provided by the input. After executing all iterations, the output will consist of pairs of identical numbers from the list `a`, printed in the order they were found, with each pair separated by a space. The process will stop once `ul` (the count of elements where `l[a[i] - 1]` equals 2) reaches `k * 2` or when `res` (the list containing elements where `l[a[i] - 1]` equals 1) is exhausted. If `ul` does not equal `ur` (the count of elements where `r[a[i] - 1]` equals 2) after processing all elements, the loop will print pairs of identical numbers from the second half of `a` until `ul` equals `ur`. Finally, the output will include the elements in `res` if `k` was non-zero, followed by the last value of `i` which will be `2 * n`.
    #
    #In summary, the output will display all valid pairs of identical numbers from the list `a` as specified by the conditions within the loop, and the final state of `i` will be `2 * n`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a list of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it prints pairs of identical numbers from the list `a` according to specific conditions involving `n` and `k`. The function ensures that the first half of the list `a` is fully processed before moving to the second half. If the counts of certain elements do not match, it continues processing the second half of the list. Finally, it prints any remaining elements from a result list and ends with the value `2 * n`.

