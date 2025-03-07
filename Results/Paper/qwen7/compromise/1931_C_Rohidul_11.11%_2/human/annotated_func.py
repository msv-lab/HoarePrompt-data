#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, the variable `l` will be equal to the total number of consecutive identical elements from the start of the list up to the second last element. The variable `r` will be 0, indicating that the search has gone through the entire list from the start to the end. The variable `st` will also be equal to the total number of consecutive identical elements from the start of the list up to the second last element, and `end` will be equal to the total number of consecutive identical elements from the end of the list up to the second last element plus 3 (as it was increased by 3 in each iteration). The value of `ans` will be calculated based on the final positions of `l` and `r`, and the values of `st` and `end`. Specifically, if `st` is not 0, or `end` is not 0, or the first element of the list `a[0]` is equal to the last element `a[-1]`, then `ans` will be `r - l` (which is `0 - l` or simply `-l`). Otherwise, `ans` will be `r - l - 1` (which is `-l - 1`).
    #
    #In simpler terms, after all iterations, `l` and `st` will both reflect the count of consecutive identical elements from the start of the list, `r` will be 0, `end` will reflect the count of consecutive identical elements from the end of the list plus 3, and `ans` will be the length of the list minus `l` if certain conditions are met, or `length - l - 1` otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a \). It calculates and prints the maximum length of a segment within the list \( a \) that does not contain any consecutive identical elements. If the first and last elements of the list are identical, it adjusts the calculation accordingly. The function does not return any value but prints the result for each test case.

