#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5. a_i is a list of n integers where 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: `_` is `t - 1`, `n` and `m` are specific integers provided by the user, `a` is a sorted list of integers with at least 2 elements, `c` is a sorted list of integers in descending order provided by the user, `ans` is the sum of the maximum absolute differences between corresponding elements of `a` and `c` for each iteration, `k` is `len(a) - 1`, `i` is the number of times `t1` was greater than or equal to `t2`, `j` is the number of times `t2` was greater than `t1` plus 1.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `m` and lists of integers `a` and `c`. For each test case, it calculates the minimum number of operations required to make all elements of `a` equal to the elements of `c` by either increasing or decreasing the elements of `a`. The function prints the result for each test case. If all elements in `a` and `c` are the same, it prints 0. Otherwise, it prints the sum of the maximum absolute differences between corresponding elements of `a` and `c` after sorting `a` in ascending order and `c` in descending order.

