#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2 · 10^5, representing the size of the array, and a is a list of n integers where 1 ≤ a_i ≤ n, representing the array elements. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has finished executing all iterations, and for each test case, the value of `ans` is printed, which represents the length of the array after removing the longest prefix and suffix of equal elements. The variables `t`, `n`, and `a` retain their initial values for the next test case, and the loop variables `l`, `r`, `st`, and `end` are reset for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the length of the array after removing the longest prefix and suffix of equal elements. If the array is entirely composed of equal elements, it prints 0. If the array has no equal elements in the prefix or suffix, it prints the length of the array minus 1. The function does not return any values; it only prints the results for each test case. The variables `t`, `n`, and `a` retain their initial values for the next test case, and the loop variables `l`, `r`, `st`, and `end` are reset for each test case.

