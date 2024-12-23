#State of the program right berfore the function call: The input consists of multiple lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The second line contains n integers a_1, a_2, ..., a_n (-10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `prefix_sum[0]` is `0`, `prefix_sum[i]` for `i` from `1` to `n` is the sum of the first `i` elements of `a`.
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
            
        #State of the program after the  for loop has been executed: `prefix_sum[0]` is `0`, `prefix_sum[i]` for `i` from `1` to `n` is the sum of the first `i` elements of `a`, the sum of the first `n` elements of `a` is not `0`, `k` is `n+1`, `l` is the largest index `r` such that `prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]`, and `r` is `n`
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`prefix_sum[0]` is 0, `prefix_sum[i]` for `i` from `1` to `n` is the sum of the first `i` elements of `a`. If `prefix_sum[n]` equals 0, then no changes are made. Otherwise, `k` is set to `n+1`, `l` is the largest index `r` such that `prefix_sum[r]` is neither 0 nor equal to `prefix_sum[n]`, and `n` remains unchanged.
#Overall this is what the function does:The function reads an integer `n` and an array `A` of `n` integers from the standard input. It calculates the prefix sums of the array `A` and stores them in the list `prefix_sum`. After calculating the prefix sums, the function checks if the sum of the entire array `A` is zero. If it is zero, the function prints 'NO'. Otherwise, it finds the largest index `r` such that the prefix sum up to `r` is neither zero nor equal to the total sum of the array `A`. It then prints the starting and ending indices `k` and `l` for each subarray whose sum is non-zero and not equal to the total sum. The function finally prints `k` and `l` again for the entire array `A`.

Potential edge cases and missing functionality:
1. If the input array `A` is empty (i.e., `n` is 0), the function does not handle this case. In practice, the function would need to check for this condition and possibly handle it appropriately.
2. The function assumes that the input values for `n` and the elements of `A` are within the specified ranges (1 ≤ n ≤ 100 and -10^3 ≤ a_i ≤ 10^3). However, it does not validate these inputs, which could lead to unexpected behavior if the inputs are out of range.
3. The function correctly handles the case where the sum of the entire array `A` is zero, printing 'NO' and not finding any subarrays. This is correctly reflected in the postcondition.
4. The function correctly identifies the largest index `r` such that the prefix sum up to `r` is neither zero nor equal to the total sum of the array `A`. This ensures that the printed subarrays cover all valid segments.

