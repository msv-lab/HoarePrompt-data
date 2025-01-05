#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the list of integers contains exactly n elements where each element is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `maximum_count` is the maximum count of 1s found in all possible toggled versions of the map `a`; `b` is a list of integers that may contain toggled values based on the indices from all possible pairs of `start` and `end`.
    print(maximum_count)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list of `n` integers (each either 0 or 1). It computes the maximum number of 1s that can be obtained by toggling any contiguous subarray of the list. The result is printed as the maximum count of 1s found after all possible toggling operations.

