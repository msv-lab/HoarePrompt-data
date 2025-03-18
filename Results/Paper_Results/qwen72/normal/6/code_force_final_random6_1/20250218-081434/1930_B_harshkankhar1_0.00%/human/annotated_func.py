#State of the program right berfore the function call: The function should take a single integer n as input, where 3 ≤ n ≤ 10^5, and n is the length of the permutation p.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [n, 2, n-2, 4, n-4, 6, ..., 1] (where n is the length of the permutation p and the list a is constructed as described)
#Overall this is what the function does:The function `func_1` accepts an integer `n` (3 ≤ n ≤ 10^5) and prints a permutation of length `n` where the elements at even indices (0, 2, 4, ...) are reversed, and the elements at odd indices (1, 3, 5, ...) remain in their original order. The function does not return any value.

