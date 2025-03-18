#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) representing the size of the array, and a list of `n` integers `a` (1 ≤ a_i ≤ n) representing the array elements. The function should be able to process up to `t` (1 ≤ t ≤ 10^4) test cases, with the sum of `n` across all test cases not exceeding 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: The loop processes all test cases, and for each test case, it prints the value of `ans`. The variables `t`, `n`, and `a` are not retained between test cases, and the loop continues to the next test case after processing the current one. The final state of the loop is that all test cases have been processed and their respective `ans` values have been printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` and a list of `n` integers `a`. For each test case, it calculates and prints a value `ans`, which represents the difference between the length of the list `a` and the maximum length of consecutive equal elements from either the start or the end of the list. If the first and last elements of the list are equal, it adjusts `ans` to account for this by subtracting the sum of the lengths of consecutive equal elements from both the start and the end. The function does not return any values; it only prints the result for each test case. After processing all test cases, the function concludes, and no state is retained between test cases.

