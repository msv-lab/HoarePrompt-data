#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and A is a list of n integers where each integer is in the range of -1000 to 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `prefix_sum` is equal to a list where `prefix_sum[i]` is the sum of the first `i` elements of `A`, for `i` from 0 to `n`, `A` is a list of `n` integers, `n` is between 1 and 100.
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
            
        #State of the program after the  for loop has been executed: `prefix_sum` is a list where `prefix_sum[i]` is the sum of the first `i` elements of `A` for `i` from 0 to `n`, `A` is a list of `n` integers where `n` is between 1 and 100, and the sum of all elements in `A` is not equal to 0. If `prefix_sum[r]` is not equal to 0 and is not equal to `prefix_sum[n]`, then `k` is equal to the number of valid `r` values that satisfy the condition, `l` is equal to the last valid `r`, and `r` will be equal to `n` after the loop finishes executing. If no `r` satisfies the condition, `k` remains 1, `l` remains 1, and `r` will be `n`.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`prefix_sum` is a list where `prefix_sum[i]` is the sum of the first `i` elements of `A`, for `i` from 0 to `n`, and `A` is a list of `n` integers with `n` between 1 and 100. If the sum of all elements in `A` is 0, 'NO' is printed. Otherwise, the sum of all elements in `A` is not equal to 0, `k` is equal to the number of valid `r` values that satisfy the condition, `l` is equal to the last valid `r`, and `r` is equal to `n`.
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `A` of `n` integers (each between -1000 and 1000). It calculates the prefix sum of `A` and checks if the total sum of `A` is zero. If the sum is zero, it prints 'NO'. If the sum is not zero, it prints 'YES' and identifies and prints sequences of indices where the prefix sum is neither zero nor equal to the total sum, followed by the indices `k`, `l`, and `n`. The function does not return any values but outputs the results directly.

