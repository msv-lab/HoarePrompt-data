#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The second line contains n integers a_1, a_2, ..., a_n (-10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `prefix_sum` is a list of length `n + 1` where each element is calculated as the cumulative sum of the first `i` elements of the list `a`, `a` is a list of integers based on the input, `prefix_sum[0]` is always 0, `prefix_sum[i + 1]` for `0 <= i < n` is the sum of the first `i + 1` elements of `a`.
    if (prefix_sum[n] == 0) :
        print('NO')
    else :
        print('YES')
        k = 1
        l = 1
        for r in range(1, n + 1):
            if prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]:
                print(k, l, r)
                k += 1
                l = r
            
        #State of the program after the  for loop has been executed: `n` must be a positive integer, `k` is the number of times the condition `prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]` was met plus 1, `l` is the last value of `r` that satisfied the condition, or 1 if no such `r` exists, `prefix_sum` is a list of length `n + 1` where each element is calculated as the cumulative sum of the first `i` elements of the list `a`, `prefix_sum[0]` is always 0, `prefix_sum[i + 1]` for `0 <= i < n` is the sum of the first `i + 1` elements of `a`, `prefix_sum[n]` is not equal to 0.
        print(k, l, n)
    #State of the program after the if-else block has been executed: `n` is a positive integer, `prefix_sum` is a list of length `n + 1` where each element is calculated as the cumulative sum of the first `i` elements of the list `a`, `prefix_sum[0]` is always 0, and `prefix_sum[i + 1]` for `0 <= i < n` is the sum of the first `i + 1` elements of `a`. If `prefix_sum[n]` is 0, the console displays 'NO'. Otherwise, `k` is the number of times the condition `prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]` was met plus 1, `l` is the last value of `r` that satisfied the condition, or 1 if no such `r` exists, and `prefix_sum[n]` is not equal to 0. The values of `k`, `l`, and `n` are printed.
#Overall this is what the function does:The function reads an integer \( n \) (1 ≤ \( n \) ≤ 100) followed by \( n \) integers \( a_1, a_2, \ldots, a_n \) (-10^3 ≤ \( a_i \) ≤ 10^3), calculates the prefix sums of the array \( A \), and checks if there is a subarray whose sum is zero. If such a subarray exists, it prints "YES" along with the indices of the subarray. If no such subarray exists, it prints "NO". The function handles the case where the entire array sums to zero by printing "NO". Additionally, if multiple subarrays with zero sum exist, it only prints one such subarray.

