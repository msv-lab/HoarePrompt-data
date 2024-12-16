#State of the program right berfore the function call: The input is a list of integers representing the array \(a\) of length \(n\), where \(1 \le n \le 100\) and \(1 \le a_1 < a_2 < \ldots < a_n \le 10^3\).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` must be greater than 0, `max_erase` is the maximum of its original value and `a[i] - a[i - 1] - 1` for all `i` in the range 1 to `n-1`.
    print(max_erase)
#Overall this is what the function does:The function accepts a list of integers representing the array \(a\) and returns the maximum number of elements that can be erased between consecutive elements such that the difference between consecutive elements minus one is maximized.

