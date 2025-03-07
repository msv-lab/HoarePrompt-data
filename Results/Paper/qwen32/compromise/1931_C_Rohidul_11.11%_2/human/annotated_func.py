#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has processed all `t` test cases, and the final output state is the result of the last test case processed. The variables `l`, `r`, `st`, `end`, and `ans` reflect the state of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints a value that represents the length of the longest contiguous subarray in `a` that can be removed such that the first and last elements of the remaining array are different. If all elements are the same, it returns the length of the array minus one. If no elements can be removed while keeping the first and last elements different, it returns 0.

