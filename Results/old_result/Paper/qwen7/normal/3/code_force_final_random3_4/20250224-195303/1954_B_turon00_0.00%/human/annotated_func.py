#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: After all iterations of the loop, `t` will be 0, `ans` will be the minimum value among all calculated `cnt` values across all test cases, `tmp` will be the first element of the list `a` from the last test case processed, `aa` will be a set containing all unique elements from the list `a` of the last test case, and `n` will be the length of the list `a` from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a list `a` of `n` integers, and implicitly an integer `t`. For each test case, it determines if the list `a` is beautiful (i.e., all elements are the same). If `a` is beautiful, it prints `-1`. Otherwise, it calculates the minimum count of consecutive occurrences of the first element in `a` and prints this value. The function outputs the minimum such count across all test cases.

