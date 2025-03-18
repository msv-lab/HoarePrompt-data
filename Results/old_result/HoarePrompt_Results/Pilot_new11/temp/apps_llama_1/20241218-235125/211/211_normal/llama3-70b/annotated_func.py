#State of the program right berfore the function call: the input array A is a list of integers, with a length n where 1 ≤ n ≤ 100, and each integer in the list is between -10^3 and 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `A` is a list of integers with a length of `n`, `a` is a list of `n` integers, `n` is a non-negative integer, `prefix_sum` is a list of `n + 1` integers where `prefix_sum[i]` is the sum of all elements in `a` up to index `i-1`, and `i` is `n-1` if `n` is greater than 0, or `prefix_sum` is a list of `n + 1` zeros and `i` is undefined if `n` is 0.
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
            
        #State of the program after the  for loop has been executed: `A` is a list of integers with a length of `n`, `a` is a list of `n` integers, `n` is a non-negative integer, `prefix_sum` is a list of `n + 1` integers where `prefix_sum[i]` is the sum of all elements in `a` up to index `i-1`, `i` is `n-1` if `n` is greater than 0, `k` is greater than or equal to 1, `l` is the last `r` where `prefix_sum[r]!= 0 and prefix_sum[r]!= prefix_sum[n]` or 1 if no such `r` exists, `r` is `n`, and 'YES' has been printed.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`A` is a list of integers with a length of `n`, `a` is a list of `n` integers, `n` is a non-negative integer, `prefix_sum` is a list of `n + 1` integers where `prefix_sum[i]` is the sum of all elements in `a` up to index `i-1`, `i` is `n-1` if `n` is greater than 0, or `prefix_sum` is a list of `n + 1` zeros and `i` is undefined if `n` is 0. If `prefix_sum[n]` is 0, then 'NO' has been printed. Otherwise, 'YES' has been printed, and `k`, `l`, `n` have been printed, where `k` is greater than or equal to 1, `l` is the last `r` where `prefix_sum[r]!= 0 and prefix_sum[r]!= prefix_sum[n]` or 1 if no such `r` exists, and `r` is `n`.
#Overall this is what the function does:The function processes a list of integers, provided through user input, with a length between 1 and 100, and each integer ranging from -10^3 to 10^3. It calculates the prefix sum of the input list and checks if the total sum of the list is zero. If the total sum is zero, it prints 'NO'. Otherwise, it prints 'YES' followed by a series of indices that represent the start and end points of subsequences where the sum of elements is non-zero and not equal to the total sum of the list. The function then prints the count of such subsequences, the start index of the last subsequence, and the total length of the list. The function handles edge cases where the input list has a length of 1, where the total sum is zero, and where there are no subsequences with a non-zero sum that is not equal to the total sum. The function does not return any value but instead prints the results directly. If the input list is empty (i.e., the user inputs 0), the function will still execute without errors, printing 'NO' because the total sum of an empty list is considered zero. The function assumes that the user will provide valid input and does not perform any error checking.

