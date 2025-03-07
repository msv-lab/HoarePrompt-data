#State of the program right berfore the function call: The function `func_1` should take a single integer `n` as input, where 3 ≤ n ≤ 10^5, and `n` is the length of the permutation `p`. The function should ensure that the input `n` is a positive integer within the specified range.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [n, 2, n-2, 4, n-4, 6, ..., 1] (where the elements at even indices are reversed and the elements at odd indices remain unchanged)
#Overall this is what the function does:The function `func_1` accepts a single integer `n` where 3 ≤ n ≤ 10^5. It generates a list `a` containing the integers from 1 to `n` in ascending order. The function then reverses the elements at even indices (0, 2, 4, ...) while keeping the elements at odd indices (1, 3, 5, ...) unchanged. Finally, it prints the modified list `a`. The function does not return any value.

