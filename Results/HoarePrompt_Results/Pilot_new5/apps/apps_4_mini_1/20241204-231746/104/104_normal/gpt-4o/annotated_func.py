#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `max_erase` is the maximum gap between consecutive elements in the list `a`, minus 1, `n` is the total number of elements in `a`, and `a` is a sorted list of `n` integers where 1 <= `a[0]` < `a[1]` < ... < `a[n-1]` <= 1000.
    print(max_erase)
#Overall this is what the function does:The function accepts a positive integer `n` and a sorted list `a` of `n` integers. It calculates the maximum gap between consecutive elements in the list `a` (minus 1), and prints this maximum gap. The function does not handle cases where `n` is 1, as there would be no gaps to compute, leading to an output of 0 in such cases. Therefore, if `n` is 1, the function will simply output 0.

