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
        
    #State: All iterations of the loop have been executed, with `l` equal to `r - k`, where `k` is the total number of iterations the loop ran. `r` is `n - k - 1`. `st` is the total number of consecutive duplicates found throughout all iterations. `end` is `k`. If `a[0] == a[-1]`, then `ans` is `r - l - 1`. Otherwise, if `st == 0`, `end == 0`, and `a[0] != a[-1]`, then `ans` is `len(a) - 1`. Otherwise, `ans` is `r - l`
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (length of the list), and a list \( a \) of \( n \) integers. It then calculates and prints the maximum value among \( r - l - 1 \), \( n - 1 \), and \( r - l \), based on certain conditions involving consecutive duplicates in the list.

