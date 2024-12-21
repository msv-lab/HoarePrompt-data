#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer where `1 <= n <= 100`, `a` is a list of `n` integers where `1 <= a[0] < a[1] < ... < a[n-1] <= 1000`, `max_erase` is the maximum length of consecutive subarrays satisfying the condition `a[k] - a[i] = k - i` for all valid indices `i` and `j` with `0 <= i < n` and `i < j <= n`.
    print(max_erase)
#Overall this is what the function does:The function reads an integer `n` representing the number of elements and a list `a` of `n` strictly increasing integers. It evaluates all possible continuous subarrays within `a` to determine the maximum number of elements that can be 'erased' (i.e., elements that do not fit the criteria of having sequential differences that match their indices). It identifies the largest such subarray where the condition `a[k] - a[i] == k - i` holds true for all valid indices `i` and `j`. The maximum number of elements that can be erased is printed as the output. Edge cases include situations where no elements can be erased, leading to a result of 0, and handling the smallest possible value for `n`. There is no return statement in the code; instead, it relies on printing the result directly.

