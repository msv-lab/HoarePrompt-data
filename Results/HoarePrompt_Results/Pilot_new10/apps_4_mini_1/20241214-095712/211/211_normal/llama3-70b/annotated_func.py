#State of the program right berfore the function call: n is an integer between 1 and 100, and A is a list of n integers where each integer a_i is in the range of -1000 to 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `prefix_sum` is a list where `prefix_sum[i]` is equal to the sum of the first `i` elements of `a` for `i` from `0` to `n`, `a` is equal to `A`, `A` is a list of length `n` containing integers from input.
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
            
        #State of the program after the  for loop has been executed: `n` is between 1 and 100, `prefix_sum` is a list where `prefix_sum[i]` is equal to the sum of the first `i` elements of `a` for `i` from `0` to `n`, `a` is equal to `A`, with `A` being a list of length `n` containing integers, and the value of `prefix_sum[n]` is not equal to 0. If there are values of `r` from 1 to `n` such that `prefix_sum[r]` is not equal to 0 and `prefix_sum[r]` is not equal to `prefix_sum[n]`, then `k` is equal to the count of such valid `r` values plus 1, `l` is equal to the last valid `r` where the condition held true, and `r` takes its final value after the last iteration of the loop where `r` is equal to `n`. If there are no such `r` values, then `k` remains 1, `l` remains 1, and `r` equals `n`.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is between 1 and 100. If `prefix_sum[n]` is equal to 0, then 'NO' is printed. Otherwise, `k` is equal to the count of valid `r` values plus 1, or 1 if no valid `r` values exist. `l` takes the last valid `r` value, or remains 1 if no such `r` values exist, and `r` is finally set to `n`.
#Overall this is what the function does:The function reads an integer `n` (between 1 and 100) followed by a list of `n` integers (each between -1000 and 1000). It computes a prefix sum of the list and checks if the total sum of the list (the last element of the prefix sum) is zero. If the total sum is zero, it prints 'NO'. Otherwise, it prints 'YES' and counts the indices `r` where the prefix sum at `r` is not zero and not equal to the total sum, printing these indices along with a final index `n`. It does not return any values but outputs results directly to the console. Additionally, if all prefix sums are zero, only 'NO' is printed, without any further output.

