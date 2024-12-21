#State of the program right berfore the function call: n is a single integer in the range 1 ≤ n ≤ 100, and A is a list of n integers where each integer a_i satisfies -10^3 ≤ a_i ≤ 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `prefix_sum` is a list where `prefix_sum[i]` is equal to the sum of the first `i` elements of the list `a`, `n` is an input integer in the range 1 ≤ `n` ≤ 100, `a` is a list of `n` integers satisfying -1000 ≤ `a_i ≤ 1000, and `prefix_sum[0]` is 0.
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
            
        #State of the program after the  for loop has been executed: `prefix_sum` is a list where `prefix_sum[i]` is equal to the sum of the first `i` elements of the list `a`, `n` is an input integer in the range 1 ≤ `n` ≤ 100, `a` is a list of `n` integers satisfying -1000 ≤ `a_i ≤ 1000, `k` is equal to the number of valid indices `r` such that `prefix_sum[r]` is not equal to 0 and `prefix_sum[r]` is not equal to `prefix_sum[n]`, and `l` is equal to the last index `r` that satisfied the condition. If no such `r` exists, `k` remains 1 and `l` remains 1.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`prefix_sum` is a list where `prefix_sum[i]` is the sum of the first `i` elements of the list `a`, `n` is an integer in the range 1 ≤ `n` ≤ 100, and `a` is a list of `n` integers satisfying -1000 ≤ `a_i ≤ 1000 with `prefix_sum[0]` equal to 0. If `prefix_sum[n]` equals 0, then 'NO' is printed indicating that the sum of all elements in the list `a` is 0. Otherwise, `k` represents the number of valid indices `r` where `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, and `l` is the last index `r` that satisfies this condition, with the output `print(k, l, n)` produced.
#Overall this is what the function does:The function takes an integer `n` and a list of `n` integers as input. It calculates the prefix sums of the list, determining the cumulative sums of the elements up to each index. If the total sum (`prefix_sum[n]`) is zero, it prints 'NO'. If the total sum is not zero, it prints 'YES' and counts the number of valid indices `r` where the prefix sum at `r` is neither zero nor equal to the total sum. For each valid index found, it prints the count of valid indices (`k`), the last valid index (`l`), and the value `n`. Finally, it also prints `k, l, n` which represent the count of valid indices, the last position that met the condition, and the total number of elements, respectively. If there are no valid indices, `k` remains 1 and `l` remains 1, indicating that the algorithm has a predetermined output in such cases. This function effectively assesses the sum characteristics of the input list and provides significant insights into its structure.

