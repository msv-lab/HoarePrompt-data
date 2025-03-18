#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum absolute difference between elements of the sorted lists `a` and `c` after applying the specified logic. The variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged as they are not modified within the loop. The loop variables `i`, `j`, and `ans` are reset for each test case, so they do not retain any values between test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m`, and two lists of integers `a` and `c`. For each test case, it calculates and prints the sum of the maximum absolute differences between elements of the sorted lists `a` and `c` after applying a specific logic. If all elements in `a` and `c` are the same, it prints 0. If `a` has only one element, it prints the maximum absolute difference between that element and the elements in `c`. The function does not modify the input variables `t`, `n`, `m`, `a`, or `c` between test cases.

