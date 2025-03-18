#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n <= m <= 2 * 10^5. a_i is a list of n integers where each a_i satisfies 1 <= a_i <= 10^9. b_i is a list of m integers where each b_i satisfies 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 100.
#Overall this is what the function does:The function processes `t` test cases, each involving two lists of integers `a` and `b` of lengths `n` and `m` respectively. For each test case, it calculates and prints a result based on the differences between elements of the two lists after sorting `a` in ascending order and `b` in descending order. The result is the sum of the maximum absolute differences between corresponding elements of the sorted lists, considering specific conditions for uniform lists.

