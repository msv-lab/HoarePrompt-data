#State of the program right berfore the function call: The input consists of multiple lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The next line contains n integers a_1, a_2, ..., a_n (-10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
def func():
    n = int(input())

a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        
    #State of the program after the  for loop has been executed: n is 4, i is 3, prefix_sum is [0, 1, -1, 2, -2]
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
            
        #State of the program after the  for loop has been executed: `n` is 4, `i` is 3, `prefix_sum` is [0, 1, -1, 2, -2], `k` is 3, `l` is 2, `r` is 4.
        print(k, l, n)
    #State of the program after the if-else block has been executed: *`n` is 4, `i` is 3, and `prefix_sum` is [0, 1, -1, 2, -2]. If `prefix_sum[4]` is 0, no changes are made. Otherwise, `k` is 3, `l` is 2, and `r` is 4.
#Overall this is what the function does:The function accepts a list of integers specified by an integer `n` on the first line and the list elements on the next line. It computes the prefix sum of the input list and checks if the last element of the prefix sum array is zero. If it is zero, the function prints 'NO'. Otherwise, it finds the smallest subarray whose sum is non-zero and prints the indices of its start and end along with its length. The function returns nothing, but prints the results to the console. Potential edge cases include an empty list or a list where all elements sum to zero.

