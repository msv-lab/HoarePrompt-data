#State of the program right berfore the function call: The input will contain two lines. The first line is a single integer n (1 ≤ n ≤ 100), representing the number of elements in the array A. The second line contains n integers a_1, a_2,..., a_{n} (-10^3 ≤ a_{i} ≤ 10^3), representing the elements of the array A.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `a` is a list of `n` integers, `prefix_sum` is a list where `prefix_sum[i]` equals the sum of the first `i` elements of `a` for `i` ranging from 0 to `n`, and `i` is `n-1`.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `a` is a list of `n` integers, `prefix_sum` is a list where `prefix_sum[i]` equals the sum of the first `i` elements of `a` for `i` ranging from 0 to `n`, `i` is `n-1`, the sum of all elements in `a` (or `prefix_sum[n]`) is not equal to 0, 'YES' has been printed, `k` is 1 plus the number of `r` values for which `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, `l` is the last `r` for which `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, or 1 if no such `r` exists.
        print(k, l, n)
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and 100, `a` is a list of `n` integers, `prefix_sum` is a list where `prefix_sum[i]` equals the sum of the first `i` elements of `a` for `i` ranging from 0 to `n`, and `i` is `n-1`. If `prefix_sum[n]` is 0, 'NO' has been printed to the console. Otherwise, 'YES' has been printed, `k` is 1 plus the number of `r` values for which `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, `l` is the last `r` for which `prefix_sum[r]` is not equal to 0 and not equal to `prefix_sum[n]`, or 1 if no such `r` exists, and the values of `k`, `l`, `n` have been printed.
#Overall this is what the function does:The function accepts input in the form of two lines: the first line containing an integer n, and the second line containing n integers representing the elements of array A. It calculates the prefix sum of the array and checks if the total sum is zero. If the total sum is zero, it prints 'NO'. Otherwise, it prints 'YES' followed by a series of triples (k, l, r) where k is the index of the subarray, l is the starting index of the subarray, and r is the ending index of the subarray, such that the sum of the elements in the subarray is not equal to zero and not equal to the total sum, and finally prints the triple (k, l, n) representing the last subarray. The function handles all potential edge cases, including arrays with a single element, arrays with all elements as zero, and arrays with a mix of positive and negative numbers. If the input array has a total sum of zero, the function only prints 'NO'. If the input array has a non-zero total sum, the function prints 'YES' followed by the specified triples, which may include duplicate or overlapping subarrays if the prefix sum at any index is not equal to zero and not equal to the total sum. The function does not perform any error handling for invalid inputs, such as non-integer inputs or arrays with more or fewer elements than specified by the input integer n.

