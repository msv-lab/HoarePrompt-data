#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
        i, ans = 0, 0
        
        while i < len(a) // 2:
            ans += abs(a[i] - c[i])
            i += 1
        
        j = len(c) - len(a) + i
        
        while i < len(a):
            ans += max(abs(a[i] - c[i]), abs(a[i] - c[j]))
            i += 1
            j += 1
        
        print(ans)
        
    #State: The loop iterates through each test case, and for each test case, it prints the calculated value of `ans`. After all iterations, the variables `t`, `n`, `m`, `a_i`, and `b_i` retain their initial values, but the internal variables `a`, `c`, `i`, and `ans` are reset for each test case. The final state of the loop is that all test cases have been processed, and the corresponding `ans` values have been printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `m`, and two lists of integers `a` and `c` (renamed from `a_i` and `b_i` in the annotations). For each test case, it calculates and prints a value `ans` which represents the sum of the absolute differences between elements of the sorted list `a` and the reverse-sorted list `c`. If all elements in `a` and `c` are the same, it prints `0`. The function does not return any values; it only prints the results. After processing all test cases, the function completes, and the variables `t`, `n`, `m`, `a_i`, and `b_i` retain their initial values, but the internal variables `a`, `c`, `i`, and `ans` are reset for each test case.

