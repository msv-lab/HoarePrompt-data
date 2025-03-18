#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `t` test cases are processed. For each test case, if all elements in the list `a` are the same, `-1` is printed; otherwise, the minimum length of consecutive segments with the same number is printed.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` representing the number of test cases, an integer `n` representing the size of the list `a`, and a list `a` of `n` integers. If all elements in the list `a` are the same, it prints `-1`. Otherwise, it prints the minimum length of consecutive segments with the same number in the list `a`.

