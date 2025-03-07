#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n). The sum of n for all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        l, r = 0, n - 1
        
        st, end = 0, 0
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        if a[0] == a[-1]:
            ans = r - l - 1
        elif st == 0 and end == 0 and a[0] != a[-1]:
            ans = len(a) - 1
        else:
            ans = r - l
        
        print(max(0, ans))
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum length of the subarray that does not contain any consecutive equal elements, or 0 if the entire array consists of equal elements. The variables `t`, `n`, and `a` are not modified in the final output state, but the loop has processed all test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then calculates and prints the maximum length of a subarray within `a` that does not contain consecutive equal elements. If the entire array consists of equal elements, it prints 0. The function does not modify the input variables `t`, `n`, or `a` and processes all test cases provided.

