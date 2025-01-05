#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the list of integers a contains exactly n elements where each element is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to 100, `maximum_count` is the maximum count of flipped elements in `b` over all iterations, `start` is equal to `n - 1`, `end` is equal to `n - 1`, `count` is the sum of elements in the last updated `b`, and `b` reflects the final state of the flipped elements from `a` after all iterations.
    print(maximum_count)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` containing exactly `n` elements that are either 0 or 1. It calculates the maximum possible count of 1s in the list `b` after flipping a contiguous subarray of `a` (where flipping means changing 0s to 1s and 1s to 0s) for all possible subarrays. The function prints the maximum count of 1s obtained after all possible flips. However, it does not return any value; it only prints the result.

