#State of the program right berfore the function call: The input consists of multiple lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The second line contains n integers a_1, a_2, ..., a_n ( - 10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
def func():
    n = int(input())

a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `i` is `n`; `prefix_sum[1]` is `a[0]`; `prefix_sum[2]` is `a[0] + a[1]`; ...; `prefix_sum[n+1]` is the sum of all elements in `a`; `n` remains unchanged.
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
            
        #State of the program after the  for loop has been executed: `i` is `n`, `prefix_sum[1]` is `a[0]`, `prefix_sum[2]` is `a[0] + a[1]`, ..., `prefix_sum[n+1]` is the sum of all elements in `a`, `n` remains unchanged, `k` is `m`, `l` is `m`, `r` is `m`, and `prefix_sum[n]` is not equal to `0` and `prefix_sum[r]` is not equal to `prefix_sum[n]`.
        print(k, l, n)
    #State of the program after the if-else block has been executed: `i` is `n`, `prefix_sum[1]` is `a[0]`, `prefix_sum[2]` is `a[0] + a[1]`, ..., `prefix_sum[n+1]` is the sum of all elements in `a`, `n` remains unchanged. If `prefix_sum[n]` is 0, the function does not change any additional variables. If `prefix_sum[n]` is not 0 or `prefix_sum[r]` is not equal to `prefix_sum[n]`, `k`, `l`, and `r` are all set to `m` and `prefix_sum[n]` is not 0.
#Overall this is what the function does:The function processes an input array \(A\) consisting of \(n\) integers. It calculates the prefix sums of the array and checks if there exists a subarray whose sum is zero. If such a subarray exists, the function prints the starting and ending indices of the subarray along with the count of valid subarrays found. If no subarray with a sum of zero exists, it prints "NO". The function does not return any value. Potential edge cases include when the entire array sums to zero or when the array contains only positive or negative numbers. If the array sum is zero, the function will still correctly identify the subarray indices. If the array contains only positive or negative numbers, the function will correctly identify that no subarray sums to zero.

