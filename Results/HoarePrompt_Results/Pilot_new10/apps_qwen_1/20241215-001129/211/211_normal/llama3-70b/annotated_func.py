#State of the program right berfore the function call: The input consists of multiple lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The second line contains n integers a_1, a_2, ..., a_n ( - 10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer representing the number of elements in the array A, `a` is a list of `n` integers, `prefix_sum` is a list where each element `prefix_sum[i]` (for `0 <= i <= n`) is the sum of the first `i` elements of the list `a`, `i` is `n + 1`, and `n` must be non-negative.
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
            
        #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a list of `n` integers, `prefix_sum` is a list where each element `prefix_sum[i]` (for `0 <= i <= n`) is the sum of the first `i` elements of the list `a`, `i` is `n + 1`, `prefix_sum[n]` is not equal to `0`, `k` is the number of iterations the loop executed plus `1`, `l` is the last value of `r` for which the condition `prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]` was satisfied, and `r` is `n + 1`.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer representing the number of elements in the array `A`, `a` is a list of `n` integers, `prefix_sum` is a list where each element `prefix_sum[i]` (for `0 <= i <= n`) is the sum of the first `i` elements of the list `a`, `i` is `n + 1`. If `prefix_sum[n]` equals 0, the value printed is 'NO'. Otherwise, `k` is the number of iterations the loop executed plus 1, `l` is the last value of `r` for which the condition `prefix_sum[r] != 0 and prefix_sum[r] != prefix_sum[n]` was satisfied, and the values of `k`, `l`, and `n` are printed.
#Overall this is what the function does:The function reads an array A of size n from the input, computes the prefix sums of the array, and prints 'NO' if the sum of the entire array is zero. Otherwise, it finds and prints the smallest subarray whose sum is not zero, along with its start and end indices.

