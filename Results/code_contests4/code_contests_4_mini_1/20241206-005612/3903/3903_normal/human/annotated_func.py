#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer is either 0 or 1.
def func():
    n = int(input())
    a = map(int, raw_input().split())
    maximum_count = 0
    for start in range(0, n):
        for end in range(0, n):
            if start <= end:
                b = list(a)
                for i in range(start, end + 1):
                    b[i] = 1 - b[i]
                count = sum(b)
                maximum_count = max(maximum_count, count)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `maximum_count` is the maximum number of toggled elements in `b` after all iterations, `start` is `n - 1`, `end` is `n - 1`, and `count` is the sum of the elements in `b` after the last toggling operation.
    print(maximum_count)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers where each integer is either 0 or 1. It calculates the maximum number of integers in the list that can be set to 1 by toggling a contiguous subarray of the list. The function outputs this maximum count.

