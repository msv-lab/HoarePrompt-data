#State of the program right berfore the function call: The function `func_1` should take a single integer `n` as an argument, where 3 ≤ n ≤ 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: [n, 2, n-2, 4, n-4, 6, ..., 1, n (if n is odd)] or [n, 2, n-2, 4, n-4, 6, ..., n-1 (if n is even)]
#Overall this is what the function does:The function `func_1` accepts an integer `n` where 3 ≤ n ≤ 10^5. It generates a list of integers from 1 to `n` and then reverses the elements at even indices (considering 0-based indexing). Finally, it prints the modified list in a single line, separated by spaces. The printed list alternates between the highest and lowest remaining values, starting with the highest. If `n` is odd, the list ends with 1; if `n` is even, it ends with `n-1`. The function does not return any value.

