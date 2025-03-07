#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: For each test case, the loop will print the maximum possible sum of absolute differences between elements of the sorted list `a` and the reverse-sorted list `c`. If `a` and `c` are identical and contain only one unique value, the loop will print 0. If `a` contains only one element, the loop will print the maximum absolute difference between that element and the maximum or minimum element of `c`. The initial variables `t`, `n`, `m`, `a_i`, and `b_i` will remain unchanged, but the loop will have processed all test cases.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes two integers `n` and `m` and two lists of integers `a` and `c` as input. It then calculates and prints the maximum possible sum of absolute differences between elements of the sorted list `a` and the reverse-sorted list `c`. If both `a` and `c` contain only one unique value, it prints 0. If `a` contains only one element, it prints the maximum absolute difference between that element and the maximum or minimum element of `c`. The function does not return any value but prints the result for each test case. The initial variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged, but the function processes all test cases provided.

