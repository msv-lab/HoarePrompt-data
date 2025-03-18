#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. For each test case, the first line contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. The sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a (where the elements at even indices are reversed compared to their initial state)
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it takes an integer `n` (3 ≤ n ≤ 10^5) and creates a permutation `p` of the first `n` natural numbers. It then reverses the elements at even indices of this permutation and prints the resulting list. The sum of all `n` values across all test cases does not exceed 10^5.

