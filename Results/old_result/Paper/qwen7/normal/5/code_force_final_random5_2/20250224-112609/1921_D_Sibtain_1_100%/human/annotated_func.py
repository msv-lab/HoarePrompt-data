#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
        
    #State: Output State: The loop has executed for all its iterations, meaning `k` is equal to `0` (since the loop decrements `k` from `len(a) - 1` to `0`). The variable `ans` contains the total sum of the maximum of `t1` and `t2` for each iteration, where `t1` is the absolute difference between `a[i]` and `c[i]`, and `t2` is the absolute difference between `a[len(a) - j]` and `c[len(c) - j]`. The values of `i` and `j` are the final values they attain after processing all elements of `a` and `c` according to the conditions inside the loop. `t1` and `t2` reflect the absolute differences based on these final values of `i` and `j`.
    #
    #In summary, after all iterations of the loop, `k` is `0`, `ans` is the total accumulated cost, and `i` and `j` are the final indices used to compute the differences.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n and m, followed by lists a and c. If a and c are uniform and match, it prints 0. Otherwise, it sorts a in ascending order and c in descending order. Then, it calculates the total sum of the maximum absolute differences between corresponding elements of a and c, considering specific conditions for indices i and j. Finally, it prints the total sum.

