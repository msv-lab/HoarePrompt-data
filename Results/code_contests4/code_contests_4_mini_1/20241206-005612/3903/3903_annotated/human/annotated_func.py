#State of the program right berfore the function call: n is an integer between 1 and 100 (inclusive), and a is a list of n integers where each integer is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `maximum_count` is the maximum sum of toggled values of `b` for all segments from `start` to `end`.
    print(maximum_count)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (each either 0 or 1). It computes the maximum possible sum of the list obtained by toggling all elements between any two indices `start` and `end`. The function outputs this maximum sum. However, there is a critical issue: the list `a` is not correctly initialized as it uses `raw_input()` which is not defined in Python 3, and thus, the function will raise an error when executed. The intended functionality seems to be to calculate the maximum count of 1s that can be achieved by flipping segments of the list, but due to the incorrect input handling, the function will not work as intended.

