#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100, and a is a list of n integers such that 1 ≤ a[1] < a[2] < ... < a[n] ≤ 10^3.
def func():
    n = int(input())

a = list(map(int, input().split()))

max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer where 2 ≤ n ≤ 100, `a` is a list of `n` integers such that 1 ≤ a[1] < a[2] < ... < a[n] ≤ 10^3, `max_erase` is `max(a[i] - a[i-1] - 1 for i in range(1, n))`, `i` is `n-1`.
    print(max_erase)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers from the user input. It calculates the maximum number of elements that can be erased between any two consecutive elements in the sorted list `a` without changing the order of the remaining elements. The function then prints this maximum number. The final state of the program is that `n` is an integer within the range 1 ≤ n ≤ 100, `a` is a list of `n` integers where 1 ≤ a[1] < a[2] < ... < a[n] ≤ 10^3, and `max_erase` holds the maximum difference minus one between any two consecutive elements in `a`. The function does not return any value. Edge cases include when `n` is 1 (in which case `max_erase` will be 0 since there are no pairs of elements to compare).

