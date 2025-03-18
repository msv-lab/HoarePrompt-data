#State of the program right berfore the function call: The input is a list of integers representing the array $a_1, a_2, \ldots, a_n$ where $1 \le n \le 100$ and $1 \le a_1 < a_2 < \ldots < a_n \le 10^3$.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `a` is a list of integers entered by the user, `i` is `n`, `j` is `n + 1`, `max_erase` is the maximum value of `j - i - 1` for all valid sublists `[i:j]` where `j` ranges from `i+1` to `n+1` and satisfies the condition `a[k] - a[i] == k - i` for all `k` in the range `[i, j)`, and `n` must be greater than 0.
    print(max_erase)
#Overall this is what the function does:The function accepts a list of integers representing an increasing sequence of length between 1 and 100. It then iterates over all possible sublists of the given list, checking if the elements in each sublist satisfy the condition \(a[k] - a[i] == k - i\) for all \(k\) in the range \([i, j)\). The function calculates the maximum length of such sublists and returns this maximum length as the output. If no valid sublist is found, the function returns 0.

