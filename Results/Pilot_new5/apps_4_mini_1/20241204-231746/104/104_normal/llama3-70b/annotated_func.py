#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100, `a` is a list of `n` integers from user input where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000, `max_erase` is the maximum number of erasable elements from any valid subarray within the list `a`, `i` is at least 0 and less than `n`, and `j` is not used after the loop has finished.
    print(max_erase)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` strictly increasing integers, then calculates and prints the maximum number of erasable elements from any valid subarray within `a` where the elements are contiguous and follow a specific arithmetic progression. If no valid contiguous subarray exists, it will return 0.

