#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the subsequent list of integers has length n, where each element a_i satisfies -10^3 ≤ a_i ≤ 10^3.
def func():
    n = int(input())

a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: `i` is 4, `n` is 5, `a` is [1, -2, 3, -4, 5], `prefix_sum` is [0, 1, -1, 2, -2, 3]
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
            
        #State of the program after the  for loop has been executed: `i` is 4, `n` is 5, `a` is [1, -2, 3, -4, 5], `prefix_sum` is [0, 1, -1, 2, -2, 3], `k` is 4, `l` is 3, `r` is 5.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`i` is 4, `n` is 5, `a` is [1, -2, 3, -4, 5], `prefix_sum` is [0, 1, -1, 2, -2, 3]. If `prefix_sum[n]` equals 0, the function does not change any additional variables. Otherwise, `k` is 4, `l` is 3, and `r` is 5.
#Overall this is what the function does:The function processes a list of integers of length \( n \) (where \( 1 \leq n \leq 100 \) and each element \( a_i \) satisfies \( -10^3 \leq a_i \leq 10^3 \)). It calculates the prefix sums of the list and checks if the sum of the entire list is zero. If the sum is zero, it prints 'NO'. Otherwise, it finds the minimum number of contiguous subarrays whose sums are non-zero and prints their starting and ending indices along with the index of the last element processed. The function also handles the case where the input list might be empty, although the current implementation does not explicitly handle this scenario.

