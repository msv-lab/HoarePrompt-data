#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and A is a list of n integers where each integer a_i satisfies -10^3 ≤ a_i ≤ 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer satisfying 1 ≤ `n` ≤ 100, `A` is a list of `n` integers, `a` is a list of `n` integers, `prefix_sum` is a list where `prefix_sum[0]` is 0, and `prefix_sum[i + 1]` is equal to the sum of the first `i` elements of list `a` for `i` from 0 to `n-1`.
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
            
        #State of the program after the  for loop has been executed: `k` is the count of values of `r` for which `prefix_sum[r]` is not 0 and is not equal to `prefix_sum[n]`, `l` is the last value of `r` for which the condition was met, `r` is equal to `n`, `n` is a positive integer satisfying 1 ≤ `n` ≤ 100. If the condition is never met, `k` remains 1 and `l` remains 1.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is a positive integer satisfying 1 ≤ `n` ≤ 100, `A` is a list of `n` integers, `a` is a list of `n` integers, and `prefix_sum` is a list where `prefix_sum[0]` is 0, with `prefix_sum[i + 1]` equal to the sum of the first `i` elements of list `a` for `i` from 0 to `n-1`. If `prefix_sum[n]` is 0, 'NO' is printed. Otherwise, `k` is the count of values of `r` for which `prefix_sum[r]` is not 0 and is not equal to `prefix_sum[n]`, `l` is the last value of `r` for which this condition was true, and the output is printed as `k`, `l`, `n`.
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` integers. It calculates the prefix sums of the list and checks if the total sum of the list is zero. If the total sum is zero, it prints 'NO'. Otherwise, it prints 'YES' and counts the number of non-zero prefix sums that are not equal to the total sum, printing the count and the last indices where this condition holds, followed by `n`. If all elements of the list are zero, it could lead to an ambiguous situation where no valid output is generated for the prefix sums, as the conditions depend on the existence of non-zero sums.

