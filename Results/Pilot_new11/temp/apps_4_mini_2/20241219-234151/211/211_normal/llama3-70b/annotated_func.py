#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), and A is a list of n integers where each integer a_i satisfies -1000 ≤ a_i ≤ 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100), `a` is a list of `n` integers, `prefix_sum` is a list where `prefix_sum[0]` is 0 and `prefix_sum[k]` is equal to the sum of the first `k` elements of `a` for `1 ≤ k ≤ n`, and `i` is `n - 1`.
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
            
        #State of the program after the  for loop has been executed: `k` is the count of valid indices where `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, `l` is the last valid index `r`, `r` is `n`, and `prefix_sum` is an array where `prefix_sum[0]` is 0 and `prefix_sum[r]` holds the sum of the first `r` elements of `a`.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 100), `a` is a list of `n` integers, and `prefix_sum` is a list where `prefix_sum[0]` is 0 and `prefix_sum[k]` is equal to the sum of the first `k` elements of `a` for `1 ≤ k ≤ n`. If `prefix_sum[n]` is 0, 'NO' is printed. Otherwise, `k` counts valid indices where `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, `l` is the last valid index `r`, and `r` equals `n`. The `prefix_sum` reflects the calculated sums of the elements of `a`.
#Overall this is what the function does:The function reads a positive integer `n` and a list `A` of `n` integers, computes the prefix sums for the list, and checks if the sum of the entire list is zero. If the total sum is zero, it prints 'NO'. If not, it prints 'YES' and counts the number of indices where the prefix sums are neither zero nor equal to the total sum. It prints these valid indices along with the last evaluated index. The final output includes the count of such valid indices and the last evaluated index `n`. Additionally, the function does not handle cases where the input might not meet the constraints (e.g., invalid integers or incorrect list length).

