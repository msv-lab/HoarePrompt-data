#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 100) indicating the number of elements in the array, followed by n integers a_i (1 ≤ a_1 < a_2 < ... < a_n ≤ 1000) representing a strictly increasing array.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100; `a` is a list of integers; `max_erase` is the maximum value of `a[i] - a[i - 1] - 1` for all `i` in the range from 1 to `n - 1`.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer `n`, where `n` (1 ≤ n ≤ 100) indicates the number of elements in an array, followed by `n` strictly increasing integers (1 ≤ a_1 < a_2 < ... < a_n ≤ 1000). It then calculates the maximum number of integers that can be erased between consecutive elements in the array and prints this value. If `n` is 1, the function will return 0 since there are no pairs of elements to compare.

