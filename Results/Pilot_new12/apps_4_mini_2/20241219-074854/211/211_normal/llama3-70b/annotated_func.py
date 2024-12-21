#State of the program right berfore the function call: The input n is an integer (1 ≤ n ≤ 100) representing the number of elements in the array A, and A is a list of n integers where each integer a_i satisfies -1000 ≤ a_i ≤ 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is an input integer (1 ≤ n ≤ 100), `i` is equal to `n - 1`, `prefix_sum` is a list of length `n + 1` where `prefix_sum[j]` is equal to the sum of the first `j` elements of the list `a` for `j` in the range [0, n]. If the loop does not execute (if `n` is 0), `prefix_sum` remains a list of length 1 filled with zero.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `k` is the count of valid `r` values found plus 1, `l` is equal to the last valid `r` where `prefix_sum[r]` was updated, if loop executed; if loop did not execute, `k` remains 1, `l` remains 1.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is an input integer (1 ≤ n ≤ 100). If `prefix_sum[n]` is equal to 0, the output is 'NO'. Otherwise, `k` is set to 1 and `l` is set to 1.
#Overall this is what the function does:This function processes an input integer `n` that determines the number of elements in an integer list `A`. It computes the prefix sums for the elements of `A` and checks if the total sum of the elements (`prefix_sum[n]`) is zero. If the sum is zero, it outputs 'NO'; otherwise, it outputs 'YES' followed by a sequence of indices. The function then identifies valid indices `r` where the prefix sum is neither zero nor equal to the total sum, and it outputs the count of these indices along with the last valid `l` and the total count `n`. If `n` is 0, it defaults to an output indicating no valid sums. The function also effectively handles the maximum and minimum constraints on the input values.

