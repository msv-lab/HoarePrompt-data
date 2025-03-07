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
        
    #State: The loop iterates through each test case, and for each test case, it prints the minimum number of operations required to make the list `a` equal to the list `c` by either increasing or decreasing the elements of `a` to match the elements of `c`. The variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged, but the loop's internal variables `i`, `j`, and `ans` are reset for each test case. After all iterations, the loop has no effect on the initial state variables, and the output state is the same as the initial state, except that the program has printed the results for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves two lists of integers, `a` and `c`. For each test case, it calculates and prints the minimum number of operations required to make all elements of `a` equal to the corresponding elements of `c` by either increasing or decreasing the elements of `a`. The function does not return any value; it only prints the result for each test case. After processing all test cases, the initial state variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged, and the program has printed the results for each test case.

