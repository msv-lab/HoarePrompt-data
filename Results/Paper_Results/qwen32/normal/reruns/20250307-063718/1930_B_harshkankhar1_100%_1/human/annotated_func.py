#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. For each test case, the first line contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. The sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: the elements of the list `a` after reversing the elements at even indices and keeping the elements at odd indices unchanged
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it takes an integer `n` representing the length of a permutation `p`. It then reverses the elements at even indices of the permutation while keeping the elements at odd indices unchanged, and prints the modified permutation.

