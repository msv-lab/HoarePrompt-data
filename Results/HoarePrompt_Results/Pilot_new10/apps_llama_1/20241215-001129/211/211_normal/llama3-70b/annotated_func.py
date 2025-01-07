#State of the program right berfore the function call: The input consists of a list of integers A of length n, where n is an integer such that 1 ≤ n ≤ 100 and each element in A is an integer such that -10^3 ≤ a_i ≤ 10^3 for 1 ≤ i ≤ n.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `A` has a length of `n` where 0 ≤ `n` ≤ 100, `a` has the same length as the number of input integers, `prefix_sum` is a list of length `n + 1` where each element at index `i` is the sum of all elements up to index `i-1` in `a`, `i` is `n-1` if `n` > 0, and `prefix_sum` contains all zeros if `n` is 0.
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
            
        #State of the program after the  for loop has been executed: `A` has a length of `n`, `a` has the same length as the number of input integers, `prefix_sum` is a list of length `n + 1` representing the prefix sum of `a`, `i` is `n-1` if `n` > 0, `k` is 1 plus the number of times a non-zero and non-total sum prefix was found, `l` is the last index `r` where such a prefix sum was found, and values have been printed for each such occurrence. If `n` is 0, `k` is 1, `l` is 1, and no values have been printed.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`A` has a length of `n` where 0 ≤ `n` ≤ 100, `a` has the same length as the number of input integers, `prefix_sum` is a list of length `n + 1` where each element at index `i` is the sum of all elements up to index `i-1` in `a`, `i` is `n-1` if `n` > 0, and `prefix_sum` contains all zeros if `n` is 0. If the current value of `prefix_sum` at index `n` is 0, 'NO' has been printed to the console. Otherwise, `k` is 1 plus the number of times a non-zero and non-total sum prefix was found, `l` is the last index `r` where such a prefix sum was found, values have been printed for each such occurrence, and the values of `k`, `l`, and `n` have been printed. If `n` is 0 in this case, `k` is 1, `l` is 1.
#Overall this is what the function does:The function reads a list of integers from the console, calculates the prefix sum, and prints 'NO' if the total sum is zero. If the total sum is non-zero, it prints 'YES' and the indices of non-zero prefix sums that are not equal to the total sum, as well as the final indices, but does not handle invalid inputs and may produce unexpected results for edge cases.

