#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are positive integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5 and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        c = list(map(int, input().split()))
        
        if len(set(a)) == 1 and len(set(c)) == 1 and a[0] == c[0]:
            print(0)
            continue
        
        a.sort()
        
        c.sort(reverse=True)
        
        if len(a) == 1:
            print(max(abs(a[0] - max(c)), abs(a[0] - min(c))))
            continue
        
        i, j, ans = 0, 1, 0
        
        for k in range(len(a)):
            t1 = abs(a[i] - c[i])
            t2 = abs(a[len(a) - j] - c[len(c) - j])
            if t2 > t1:
                j += 1
            else:
                i += 1
            ans += max(t1, t2)
        
        print(ans)
        
    #State: `i` is equal to `len(a)`, `j` is equal to `len(c)`, `ans` is the cumulative sum of `max(t1, t2)` for each iteration of the loop, `k` is equal to `len(a)`, `t1` is `abs(a[len(a) - 1] - c[0])`, and `t2` is `abs(a[0] - c[len(c) - 1])`
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two sequences of integers \(a\) and \(c\), sorts them, and calculates the sum of the maximum absolute differences between corresponding elements of the sorted sequences. If the sequences are identical, it prints 0. Otherwise, it prints the calculated sum. The function does not return any value but prints the result for each test case.

