#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and the second line of input contains n integers a_i such that 1 <= a_1 < a_2 < ... < a_n <= 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is an integer such that `0 <= i < n`, `j` is the last value of `j` for which the condition `all(a[k] - a[i] == k - i for k in range(i, j))` was satisfied for any subarray starting from `i` to `j-1`, and `max_erase` is the maximum value of `j - i - 1` encountered during the loop iterations.
    print(max_erase)
#Overall this is what the function does:The function processes a list of integers \(a_i\) of length \(n\) (where \(1 \leq n \leq 100\)), ensuring that each element \(a_i\) is strictly increasing and lies within the range \(1 \leq a_1 < a_2 < \ldots < a_n \leq 10^3\). It aims to find the maximum number of elements that can be erased from the list such that the remaining elements still maintain a strictly increasing order. Specifically, for every subarray of consecutive elements, it checks if the difference between each pair of elements is equal to their index difference. If such a subarray is found, it calculates the maximum length of such subarrays minus one (since we are erasing elements, not keeping them), and updates the maximum erase count accordingly. The function then prints the maximum number of elements that can be erased.

