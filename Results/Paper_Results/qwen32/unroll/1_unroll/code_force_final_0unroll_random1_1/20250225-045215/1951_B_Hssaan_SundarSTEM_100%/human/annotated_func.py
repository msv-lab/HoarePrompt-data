#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case, n is an integer such that 2 ≤ n ≤ 10^5, k is an integer such that 1 ≤ k ≤ n, and a is a list of n distinct integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j + 1
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: The output state consists of a series of integers, each being the result of the maximum of `ans` and `ans1` for each test case. The values of `t`, `n`, `k`, and `s` reflect the state after processing the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of distinct integers and two integers `n` and `k`. For each test case, it calculates and prints the maximum number of elements that can be moved to the beginning of the list under specific conditions related to the value at index `k-1`. The function outputs a series of integers, each representing the result for a corresponding test case.

