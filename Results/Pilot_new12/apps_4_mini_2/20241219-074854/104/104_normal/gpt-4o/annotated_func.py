#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range of 1 to 100, `max_erase` is the maximum gap of consecutive elements in `a` that can be erased, which is the maximum of all `a[i] - a[i - 1] - 1` for `1 <= i < n`, and `a` is a list of `n` integers where `1 <= a[0] < a[1] < ... < a[n-1] <= 1000.`
    print(max_erase)
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 <= n <= 100) and a list `a` of `n` integers that are strictly increasing and within the range of 1 to 1000. It calculates the maximum gap of consecutive elements in the list `a` that could be erased without affecting the order of the remaining elements. The result is the largest difference between adjacent elements in `a`, minus one. After the function completes, it prints this maximum gap, denoted as `max_erase`. The function does not explicitly return any value. Edge cases include scenarios where `n` is 1 (in which case there would be no gaps to calculate) and the function assumes valid input constraints without additional error handling for invalid input data.

