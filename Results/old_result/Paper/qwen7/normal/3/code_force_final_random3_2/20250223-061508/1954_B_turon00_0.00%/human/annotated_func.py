#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: After all iterations of the loop, `ans` will hold the overall minimum value of `cnt` encountered across all iterations, `t` will be 0, `i` will be `n-1`, `tmp` will be equal to the last element of the list `a`, `cnt` will be 0, and `aa` will still contain all elements of the list `a` as a set.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` representing the number of test cases, an integer `n` representing the size of the list `a`, and a list `a` of `n` integers. For each test case, it calculates the minimum length of consecutive occurrences of the same integer in the list `a`. If all elements in the list are the same, it prints `-1`. Otherwise, it prints the minimum length of such consecutive occurrences across all test cases.

